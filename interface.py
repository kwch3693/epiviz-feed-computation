import pandas as pd
from epivizFeed.ComputeObj import ComputeObj


def computational_request(start, end, chromosome, gene_name, measurements=None):
    additional_params = [None, None, {"partition_type": "condition", "group_one": "normal", "group_two": "cancer", "grouping": "all_pairs"},
            {"partition_type": "condition", "group_one": "normal", "group_two": "cancer", "grouping": "all_pairs"},
            {"partition_type": "condition", "group_one": "normal", "group_two": "tumor", "grouping": "all_pairs"},
            {"partition_type": None, "group_one": "normal", "group_two": "cancer", "grouping": "all_pairs"},
            {"partition_type": None, "group_one": "normal", "group_two": "cancer", "grouping": "all_pairs"},
            {"partition_type": None, "group_one": "normal", "group_two": "tumor", "grouping": "all_pairs"}]

    computations = ["ttest_block_expression", "block_overlap_percent",
                "expression_methydiff_correlation", "expression_methy_correlation",
                "ttest_expression_per_gene", "methy_diff_correlation", "methy_correlation",
                "expression_correlation"]
    for comp, param in zip(computations, additional_params):
        obj = ComputeObj(comp, measurements)
        yield obj.compute(chromosome, start, end, param)
