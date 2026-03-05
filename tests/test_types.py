"""Tests for the shared types module (scripts/lib/types.py)."""

from pathlib import Path

from scripts.lib.types import ConflictInfo, ReconciledTask, StoredTask


class TestConflictInfoInTypes:
    """ConflictInfo should be importable from types.py with expected structure."""

    def test_conflict_info_has_expected_fields(self):
        info = ConflictInfo(
            task_list_id="test-123",
            existing_task_count=5,
            sample_subjects=("A", "B"),
        )
        assert info.task_list_id == "test-123"
        assert info.existing_task_count == 5
        assert info.sample_subjects == ("A", "B")

    def test_conflict_info_to_dict(self):
        info = ConflictInfo(
            task_list_id="test-123",
            existing_task_count=3,
            sample_subjects=("Task A", "Task B"),
        )
        d = info.to_dict()
        assert d == {
            "task_list_id": "test-123",
            "existing_task_count": 3,
            "sample_subjects": ("Task A", "Task B"),
        }

    def test_conflict_info_source_from_reconciliation(self):
        """ConflictInfo in task_reconciliation should come from types module."""
        from scripts.lib.task_reconciliation import ConflictInfo as RC
        assert RC.__module__ == "scripts.lib.types" or RC.__module__ == "lib.types"

    def test_conflict_info_source_from_storage(self):
        """ConflictInfo in task_storage should come from types module."""
        from scripts.lib.task_storage import ConflictInfo as SC
        assert SC.__module__ == "scripts.lib.types" or SC.__module__ == "lib.types"

    def test_conflict_info_not_defined_in_reconciliation(self):
        """task_reconciliation.py should NOT define ConflictInfo locally."""
        source_path = Path(__file__).parent.parent / "scripts" / "lib" / "task_reconciliation.py"
        source = source_path.read_text()
        assert "class ConflictInfo" not in source

    def test_conflict_info_not_defined_in_storage(self):
        """task_storage.py should NOT define ConflictInfo locally."""
        source_path = Path(__file__).parent.parent / "scripts" / "lib" / "task_storage.py"
        source = source_path.read_text()
        assert "class ConflictInfo" not in source


class TestReconciledTask:
    """ReconciledTask (renamed from CurrentTask in task_reconciliation)."""

    def test_has_expected_fields(self):
        task = ReconciledTask(
            id="1", subject="Test", status="pending",
            description="desc", active_form="form",
        )
        assert task.id == "1"
        assert task.subject == "Test"
        assert task.status == "pending"
        assert task.description == "desc"
        assert task.active_form == "form"

    def test_no_current_task_in_reconciliation(self):
        """task_reconciliation.py should NOT have a class named CurrentTask."""
        source_path = Path(__file__).parent.parent / "scripts" / "lib" / "task_reconciliation.py"
        source = source_path.read_text()
        assert "class CurrentTask" not in source


class TestStoredTask:
    """StoredTask (renamed from CurrentTask in task_storage)."""

    def test_has_expected_fields(self):
        task = StoredTask(
            position=1, subject="Test", status="pending",
            description="desc", blocks=("2",), blocked_by=("0",),
        )
        assert task.position == 1
        assert task.subject == "Test"
        assert task.blocks == ("2",)
        assert task.blocked_by == ("0",)

    def test_no_current_task_in_storage(self):
        """task_storage.py should NOT have a class named CurrentTask."""
        source_path = Path(__file__).parent.parent / "scripts" / "lib" / "task_storage.py"
        source = source_path.read_text()
        assert "class CurrentTask" not in source
