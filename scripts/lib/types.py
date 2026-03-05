"""Shared type definitions for deep-plan scripts.

Centralizes dataclass definitions that are used across multiple modules
to avoid duplication and name collisions.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True, kw_only=True)
class ConflictInfo:
    """Information about a task list conflict."""

    task_list_id: str
    existing_task_count: int
    sample_subjects: tuple[str, ...]

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON output."""
        return {
            "task_list_id": self.task_list_id,
            "existing_task_count": self.existing_task_count,
            "sample_subjects": self.sample_subjects,
        }


@dataclass(frozen=True, slots=True, kw_only=True)
class ReconciledTask:
    """A task read from the task list directory (API view).

    Represents a task from the Claude Code task list, keyed by numeric ID.
    Renamed from CurrentTask in task_reconciliation.py.
    """

    id: str
    subject: str
    status: str
    description: str
    active_form: str


@dataclass(frozen=True, slots=True, kw_only=True)
class StoredTask:
    """A task read from disk (position-based).

    Represents a task stored as a JSON file, keyed by position.
    Renamed from CurrentTask in task_storage.py.
    """

    position: int
    subject: str
    status: str
    description: str = ""
    blocks: tuple[str, ...] = ()
    blocked_by: tuple[str, ...] = ()
