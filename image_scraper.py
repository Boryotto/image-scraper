from selenium import webdriver
from contextlib import contextmanager
from urlparse import urlparse
from os.path import splitext, basename, join
from urllib import urlretrieve
from argparse import ArgumentParser


def main():
    scrape_images(*parse_args())


def parse_args():
    arg_parser = ArgumentParser(
        description="Download images from a website depending on an xpath of the img's father node")
    arg_parser.add_argument('--parent-xpath', nargs=1, default="//body", type=str, required=False,
                            help="An XPATH to the parent node of the images")
    arg_parser.add_argument('--url', nargs=1, type=str, required=True,
                            help="The URL of the webpage to scrape from")
    arg_parser.add_argument('--dest', nargs=1, type=str, required=True,
                            help="The destination folder absolute path")
    arg_parser.add_argument('--trim-url', action='store_true', required=False,
                            help="Trim image urls from query strings that might make the image minified")
    arg_parser.add_argument('--webdriver-path', nargs=1, type=str, required=False, default="./chromedriver.exe",
                            help="An absolute path to a chrome Webdriver")

    namespace = arg_parser.parse_args()
    parent_xpath = namespace.parent_xpath[0]
    url = namespace.url[0]
    destination_folder = namespace.dest[0]
    trim_src_path = namespace.trim_url
    return url, parent_xpath, destination_folder, trim_src_path, webdriver


def scrape_images(url, parent_xpath, destination_folder, trim_src_path, webdriver):
    with driver_starter(webdriver_path=webdriver) as driver:
        driver.get(url=url)
        root_element = driver.find_elements_by_xpath('{}//img'.format(parent_xpath))
        image_srcs = [element.get_attribute('src') for element in root_element]
        for src in image_srcs:
            if trim_src_path:
                src = src.split('?')[0]
            parsed_url = urlparse(src)
            filename, file_ext = splitext(basename(parsed_url.path))
            dest_file_name = join(destination_folder, "{}{}".format(filename, file_ext))
            urlretrieve(src, dest_file_name)
            print dest_file_name
        print "Total: {} files saved to {}".format(len(image_srcs), destination_folder)


@contextmanager
def driver_starter(webdriver_path):
    driver = webdriver.Chrome(webdriver_path)
    yield driver
    driver.close()


if __name__ == '__main__':
    main()
