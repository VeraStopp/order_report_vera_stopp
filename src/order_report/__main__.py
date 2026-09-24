import logging
from pathlib import Path
import pandas as pd
import sys
from . import config, loading, validation, processing, reporting

logger = logging.getLogger("order_report")


class OrderReportPipeline:
    """Encapsulates the execution state and steps for order processing"""
    def __init__(self, input_path: Path, output_dir: Path) -> None:
        self.input_path = input_path
        self.output_dir = output_dir
        self.raw_df: pd.DataFrame | None = None
        self.processed_df: pd.DataFrame | None = None
        self.reports: dict[str, pd.DataFrame] = {}

    def load_and_clean(self) -> None:
        """Loads and cleans input data"""
        self.raw_df = loading.load_df(self.input_path)
        validation.validate_columns(self.raw_df)
        cleaned = validation.clean_data(self.raw_df)
        self.processed_df = processing.calculate_order_values(cleaned)

    def generate_reports(self) -> None:
        """Calculates internal summary reports"""
        if self.processed_df is None:
            raise RuntimeError("Data must be loaded before generating reports")

        self.reports = {
            "summary_by_category": processing.summarize_by_category(self.processed_df),
            "summary_by_region": processing.summarize_by_region(self.processed_df),
            "kpi_overview": processing.generate_kpi_summary(self.processed_df)
        }

    def save(self) -> None:
        """Saves generated reports to disk"""
        if not self.reports:
            raise RuntimeError("No reports available to save")

        reporting.save_all_reports(self.reports, self.output_dir)

    def run(self) -> None:
        """Executes the complete pipeline sequentially"""
        self.load_and_clean()
        self.generate_reports()
        self.save()


def main() -> None:
    """Main entry point for the order report application"""
    config.configure_logging()
    logger.info("Starting order processing pipeline")

    try:
        pipeline = OrderReportPipeline(config.INPUT_FILE_PATH, config.OUTPUT_DIR)
        pipeline.run()

        logger.info("Pipeline executed successfully")
    except Exception as error:
        logger.critical("Pipeline failed: %s", error, exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()