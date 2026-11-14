"""Tests for ModelEvaluator baseline functionality."""

import pytest
from modelaudit import ModelEvaluator


def test_import_model_evaluator():
    """Test 1: Verify ModelEvaluator can be imported directly from modelaudit."""
    import modelaudit

    assert hasattr(modelaudit, "ModelEvaluator")
    assert modelaudit.ModelEvaluator is ModelEvaluator


def test_create_model_evaluator_instance():
    """Test 2: Verify creating an instance of ModelEvaluator without arguments."""
    evaluator = ModelEvaluator()
    assert isinstance(evaluator, ModelEvaluator)


def test_run_evaluator_execution():
    """Test 3: Verify running the evaluator returns a non-empty string result."""
    evaluator = ModelEvaluator()
    result = evaluator.run()

    assert isinstance(result, str)
    assert len(result) > 0


def test_run_evaluator_result_content():
    """Test 4: Verify the returned result matches the expected baseline output format."""
    evaluator = ModelEvaluator()
    result = evaluator.run()

    expected = (
        "ModelAudit\n"
        "----------\n"
        "Evaluation engine initialized successfully.\n"
        "Status: Ready"
    )
    assert result == expected


def test_repeated_run_consistency():
    """Test 5: Verify repeated run() calls produce consistent and identical results."""
    evaluator = ModelEvaluator()

    first_result = evaluator.run()
    second_result = evaluator.run()

    assert first_result == second_result

