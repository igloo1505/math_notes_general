project = "Math Notes"
copyright = "2040, Me"
author = "Milly"

version = "0.1"

release = "0.1"

source_suffix = [".rst", ".md", ".ipynb"]
# source_suffix = ".md"

master_doc = "main"

exclude_patterns = []


html_theme = "alabaster"


html_static_path = ["static"]


# -- Extension configuration -------------------------------------------------

# -- jupyter build configuration ---------------------------------------------------
jupyter_kernels = {
    "python3": {
        "kernelspec": {
            "display_name": "Python",
            "language": "python3",
            "name": "jupyter",
        },
        "file_extension": ".py",
    },
    "python2": {
        "kernelspec": {
            "display_name": "Python",
            "language": "python2",
            "name": "python2",
        },
        "file_extension": ".py",
    },
    "julia-1.1": {
        "kernelspec": {
            "display_name": "Julia 1.1",
            "language": "julia",
            "name": "julia-1.1",
        },
        "file_extension": ".jl",
    },
}


jupyter_conversion_mode = "all"

jupyter_write_metadata = False

# Location for _static folder
jupyter_static_file_path = ["source/_static"]

# Configure jupyter headers
jupyter_headers = {
    "python3": [
        # nbformat.v4.new_code_cell("%autosave 0")      #@mmcky please make this an option
    ],
    "julia": [],
}

jupyter_welcome_block = "What the fuckkkk"

jupyter_target_html = False

jupyter_download_nb_urlpath = None

jupyter_download_nb = False


jupyter_download_nb_image_urlpath = None

jupyter_lang_synonyms = ["ipython"]

# Execute skip-test code blocks for rendering of website (this will need to be ignored in coverage testing)
jupyter_ignore_skip_test = True

# allow execution of notebooks
jupyter_execute_notebooks = False

# Location of template folder for coverage reports
jupyter_template_coverage_file_path = False

# generate html from IPYNB files
jupyter_generate_html = False

# html template specific to your website needs
jupyter_html_template = ""

# latex template specific to your website needs
jupyter_latex_template = ""

# make website
jupyter_make_site = False

# force markdown image inclusion
jupyter_images_markdown = True

# This is set true by default to pass html to the notebooks
jupyter_allow_html_only = True
