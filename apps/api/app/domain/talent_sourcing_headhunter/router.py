from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.talent_sourcing_headhunter.schemas import AgenticTalentSourcingHeadhunterSessionCreate, AgenticTalentSourcingHeadhunterSessionResponse
from app.domain.talent_sourcing_headhunter.service import AgenticTalentSourcingHeadhunterService

router = APIRouter(prefix="/api/v1/talent_sourcing_headhunter", tags=["Agentic Talent Sourcing Headhunter Domain"])

@router.post("/sessions", response_model=AgenticTalentSourcingHeadhunterSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticTalentSourcingHeadhunterSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Talent Sourcing Headhunter.
    """
    return AgenticTalentSourcingHeadhunterService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticTalentSourcingHeadhunterSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticTalentSourcingHeadhunterService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
