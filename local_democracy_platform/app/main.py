# app/main.py
from fastapi import FastAPI, Request, Form, HTTPException, Query, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from services.legislation_service import LegislationService
from services.feedback_service import FeedbackService
from services.voting_service import VotingService
from services.visualization_service import VisualizationService
from services.organizing_service import OrganizingService

app = FastAPI(title="Local Democracy Engagement Platform")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Services
legislation_service = LegislationService()
feedback_service = FeedbackService()
voting_service = VotingService()
visualization_service = VisualizationService()
organizing_service = OrganizingService()

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/legislation", response_class=HTMLResponse)
async def get_legislation(request: Request):
    return templates.TemplateResponse("legislation.html", {"request": request, "summary": None})

@app.post("/legislation", response_class=HTMLResponse)
async def post_legislation(request: Request, text: str = Form(...)):
    summary = legislation_service.summarize_legislation(text)
    return templates.TemplateResponse("legislation.html", {"request": request, "summary": summary, "text": text})

@app.get("/feedback", response_class=HTMLResponse)
async def get_feedback(request: Request):
    return templates.TemplateResponse("feedback.html", {"request": request, "submitted": False, "responses": []})

@app.post("/feedback", response_class=HTMLResponse)
async def post_feedback(request: Request, user_id: int = Form(...), representative_id: int = Form(...), message: str = Form(...)):
    fb = feedback_service.submit_feedback(user_id, representative_id, message)
    responses = feedback_service.get_feedback_responses(user_id)
    return templates.TemplateResponse("feedback.html", {"request": request, "submitted": True, "responses": responses})

@app.get("/voting", response_class=HTMLResponse)
async def get_voting(request: Request):
    polls = voting_service._polls
    return templates.TemplateResponse("voting.html", {"request": request, "polls": polls})

@app.post("/voting", response_class=HTMLResponse)
async def post_voting(request: Request, poll_id: int = Form(None), question: str = Form(None), options: str = Form(None), vote_option: str = Form(None), user_id: int = Form(None)):
    if question and options:
        opts = [opt.strip() for opt in options.split(',')]
        pid = voting_service.create_poll(question, opts)
        return RedirectResponse(url=f"/voting?poll_id={pid}", status_code=303)
    if vote_option and poll_id and user_id:
        try:
            voting_service.submit_vote(user_id, poll_id, vote_option)
        except ValueError:
            pass
        return RedirectResponse(url=f"/voting?poll_id={poll_id}", status_code=303)
    return RedirectResponse(url="/voting", status_code=303)

@app.get("/visualization", response_class=HTMLResponse)
async def get_visualization(request: Request):
    return templates.TemplateResponse("visualization.html", {"request": request})

@app.get("/visualization/data")
async def visualization_data():
    return visualization_service.policy_impact()

@app.get("/organizing", response_class=HTMLResponse)
async def get_organizing(request: Request):
    inits = organizing_service.list_initiatives()
    return templates.TemplateResponse("organizing.html", {"request": request, "initiatives": inits, "created": False})

@app.post("/organizing", response_class=HTMLResponse)
async def post_organizing(request: Request, name: str = Form(...), description: str = Form(...), neighborhood: str = Form(...)):
    organizing_service.create_initiative(name, description, neighborhood)
    inits = organizing_service.list_initiatives()
    return templates.TemplateResponse("organizing.html", {"request": request, "initiatives": inits, "created": True})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)