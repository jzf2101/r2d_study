# repo2docker study of NIPS 2017 papers 
# Presented at Learning to Be Reproducible ICML 2018

Data as part of [Reproducible Research Environments with repo2docker](https://openreview.net/forum?id=B1lYOwuoxm)

We collect data from the [NIPS 2017 schedule](https://nips.cc/Conferences/2017/Schedule) to demonstrate the relationship between the presence of [configuration files used by repo2docker](http://repo2docker.readthedocs.io/en/latest/config_files.html) and GitHub engagement.  These results are reported in Section 4 of the paper.

We use [repo2docker](https://github.com/jupyter/repo2docker) to publish a live version of the repo on [binder](https://mybinder.org).

To encourage the reproducibility of this work, we are including a link to a binder version of this repo to run our analysis in the browser. Click the button below to launch a live version of the repo on binder:

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/jzf2101/r2d_study/master?filepath=get_data.ipynb)

## Local Installation 

To install with `conda`:

```
conda env create -f environment.yml
```

We recommend exploring the repository with JuptyerLab.

```
source activate r2d-study
jupyter lab
```

If running a recent version of Jupyter Notebook or binder, you may switch to JupyterLab by replacing the part of your URL with `/tree` to `/lab`.

## File Descriptions

The majority of analysis occurs in `get_data.ipynb`.  Helper functions used in the notebook are in `collect_data.py`.  

Note: that since we use GitHub's graphql API to collect GitHub metadata, one would need to create a [personal access token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/) and replace it in the appropriate code block to recollect all the data.  The relevant collected files are included anyway as csv as described in the notebook for simplicity and exceptions are written to skip data collection if necessary.

### NIPS 2017 Datasets

The dataset with all GitHub repo data with metadata is `gh_metadata_w_labeled.csv`, indicating that this dataset includes URLs to GitHub research repos that were found through manual inspection.

The dataset with all config file information is `r2d_w_labeled.csv`.  Similarly, some URLs were found through manual inspection.

Two types of papers required manual inspection: papers that changed their GitHub repo name, or papers that had errors in their URL.  Papers that had errors in their URL are listed with their labeled URLs in `validate_url_w_labels.csv`. Papers that changed their reponame with their new repo are in `change_reponame_labeled.csv`.

Libraries that were part of larger repositories that were excluded from our analysis are in `larger_libraries.csv`. Similarly repositories that did not include lines of programming cdoe were excluded, which are listed in `no_code.csv`.