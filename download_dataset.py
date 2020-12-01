from google.cloud import storage

def download_csv():
	# Enable Storage
	client = storage.Client()
	# Reference an existing bucket.
	bucket = client.get_bucket('fake-news-detection-296619.appspot.com')
	# Download a file from your bucket.
	datasetBlob = bucket.get_blob('Fake_News_Dataset.csv')
	datasetBlob.download_to_filename('/home/fisst_projects/Fake-News-Detection/Fake_News_Dataset.csv')

def main():
	download_csv()

if __name__ == '__main__':
	main()
