from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.talent_sourcing_headhunter.models import AgenticTalentSourcingHeadhunterSession, AgenticTalentSourcingHeadhunterItem
from app.domain.talent_sourcing_headhunter.schemas import AgenticTalentSourcingHeadhunterSessionCreate, AgenticTalentSourcingHeadhunterItemCreate

class AgenticTalentSourcingHeadhunterService:
    @staticmethod
    def create_session(db: Session, data: AgenticTalentSourcingHeadhunterSessionCreate) -> AgenticTalentSourcingHeadhunterSession:
        db_obj = AgenticTalentSourcingHeadhunterSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticTalentSourcingHeadhunterSession:
        return db.query(AgenticTalentSourcingHeadhunterSession).filter(AgenticTalentSourcingHeadhunterSession.id == session_id).first()
