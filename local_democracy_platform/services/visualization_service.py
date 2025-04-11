# services/visualization_service.py
from typing import Dict
import matplotlib.pyplot as plt
import io

class VisualizationService:
    def policy_impact(self) -> Dict:
        # Stub: return dummy impact data
        return {
            "age_groups": {"18-30": 40, "31-50": 35, "51+": 25},
            "neighborhoods": {"Downtown": 50, "Uptown": 30, "Suburbs": 20}
        }

    def generate_bar_chart(self, data: Dict[str, int], title: str) -> bytes:
        fig, ax = plt.subplots()
        ax.bar(data.keys(), data.values(), color='skyblue')
        ax.set_title(title)
        ax.set_ylabel('Impact Score')
        ax.set_xlabel('Category')
        plt.xticks(rotation=45)

        buf = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close(fig)
        return buf.read()