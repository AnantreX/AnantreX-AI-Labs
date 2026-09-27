from core.pipeline import PipelineRunner

def test_pipeline_runner():
    runner = PipelineRunner(experiment_name="nlp_benchmark")
    runner.log_metric("accuracy", 0.945)
    summary = runner.summary()
    assert summary["experiment"] == "nlp_benchmark"
    assert summary["metrics"]["accuracy"] == 0.945
