# static_site_generator

This converts Markdown files into HTML files for static website generation.

## Requirements

- Python 3.11+

## Usage

1. Clone the repository
2. Create a virtual environment
3. Install the requirements if any

Directories
  * Static: Contains all the static files (CSS, images)
  * Templates: Contains the HTML templates
  * Content: Contains the Markdown files

To generate the HTML files, create a markdown file in the content directory that has a title and content.
Title <b>must</b> be present in order to run properly.

run

```
./main.sh
```
Website should be on port 8888 or specified port.

## Notes

If you want to make multiple pages having a link like this
```
[post here](/dir_name)
```
will allow for a directory to be created and serve the html page inside.
However, links for pages in the same level needs to be created separately
