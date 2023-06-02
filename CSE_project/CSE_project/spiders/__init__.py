import os
import scrapy

class ImageSpider(scrapy.Spider):
    name = "my_spider"
    start_urls = ["file:///C:/Users/nisha/Desktop/Html/Images.html"]  # Replace with the URL of the website

    def parse(self, response):
        # Extract image URLs and yield a request to download each image
        for img in response.css("img.imga1"):
            img_url = response.urljoin(img.xpath("@src").get())
            yield scrapy.Request(img_url, callback=self.save_image)

    def save_image(self, response):
        # Get the filename from the URL BY Using Split and then taking the last element
        filename = response.url.split("/")[-1]

        # Naming the directory where the images will be saved
        save_dir = "images"

        try:
            # Create the directory if it doesn't exist
            os.makedirs(save_dir, exist_ok=True)

            # Save the image to a file
            file_path = os.path.join(save_dir, filename)
            with open(file_path, "wb") as f:
                f.write(response.body)

            self.log(f"Saved file {filename} in {save_dir}")
        except Exception as e:
            self.log(f"Error saving file {filename}: {e}")