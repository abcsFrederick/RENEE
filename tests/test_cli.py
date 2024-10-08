import json
import os.path
import subprocess
import tempfile
from renee.src.renee.__main__ import main

renee_run = (
    "./main.py run "
    "--mode local --runmode init --dry-run "
    "--input .tests/*.fastq.gz "
)


def run_in_temp(command_str):
    with tempfile.TemporaryDirectory() as tmp_dir:
        outdir = os.path.join(tmp_dir, "testout")
        output = subprocess.run(
            f"{command_str} --output {outdir}",
            capture_output=True,
            shell=True,
            text=True,
        )
        if os.path.exists(os.path.join(outdir, "config.json")):
            with open(os.path.join(outdir, "config.json"), "r") as infile:
                config = json.load(infile)
        else:
            config = None
    return output, config


def test_help():
    output = subprocess.run(
        "./bin/renee --help", capture_output=True, shell=True, text=True
    ).stdout
    assert "RENEE" in output


def test_version():
    output = subprocess.run(
        "./bin/renee --version", capture_output=True, shell=True, text=True
    ).stdout
    assert "renee v" in output


def test_run_error():
    assert (
        "the following arguments are required: --output"
        in subprocess.run(
            f"{renee_run} --genome config/genomes/biowulf/hg38_36.json",
            capture_output=True,
            shell=True,
            text=True,
        ).stderr
    )


def test_subcommands_help():
    assert all(
        [
            f"renee {cmd } [--help]"
            in subprocess.run(
                f"./bin/renee {cmd} --help",
                capture_output=True,
                shell=True,
                text=True,
            ).stdout
            for cmd in ["run", "build", "cache", "unlock"]
        ]
    )


def test_default_genome():
    output, config = run_in_temp(renee_run)
    assert "No Genome+Annotation JSONs found" in output.stderr


def test_genome_param():
    output, config = run_in_temp(
        f"{renee_run} --genome config/genomes/biowulf/hg19_19.json"
    )
    assert "hg19" in config["references"]["rnaseq"]["FUSIONBLACKLIST"]
