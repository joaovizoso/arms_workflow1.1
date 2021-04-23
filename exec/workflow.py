#!/usr/bin/env python3

import split
import docManager
import preprocess
import regions
import ocr
import compare
import merge
import sys
from pathlib import Path

def to_do(doc):	
	n = doc['name']
	status = doc['status']
	path = doc['path']

	if (status['split']):
		print("Splitting %s"%n)
		split.split_pages(Path(path))	
		print("%s splitted"%n)

	if (status['preprocess']):
		print("Preprocessing %s"%n)
		preprocess.pre_process(n)
		print("%s preprocessed"%n)

	if (status['segment']):
		print("Segmenting %s"%n)
		regions.save(n)
		print("%s segmented"%n)
	
	if (status['ocr']):
		print("OCR %s"%n)
		ocr.ocr(n)
		print("%s OCR done"%n)

	if (status['compare']):
		print("Comparing results of %s"%n)
		compare.modify(n) 
		print("%s results compared"%n)

	if (status['merge']):
		print("Comparing results of %s"%n)
		merge.merge(n)
		print("%s results compared"%n)
		
	
	docManager.delete_data(n)


def main(inputFile):

	inputFile = Path(inputFile)
	docManager.write_name(inputFile)
	doc = docManager.get_data(inputFile.parts[-1])	
	to_do(doc)
	print("Done")


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python3 workflow.py inputFile")
		sys.exit(1)
	main(sys.argv[1])

