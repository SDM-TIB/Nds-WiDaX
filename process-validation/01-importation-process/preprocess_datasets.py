import sys
import json
import os

class KG_creation:

	def __init__(self, repo, outfile):
		"""
		Initialize the KG_creation class with the repository name and output file path.

		Parameters:
		----------
		repo : str
			The repository name (e.g., "GOE", "LEO", "LUH", "OSN").
		outfile : str
			The path to the output file where the preprocessed data will be saved.
		"""
		self.kg_domain = "http://localhost:5002"
		if repo == "GOE":
			self.input_folder = "Mapping_files/json_importation_files/Goettingen/json_files_mapped_to_LDM/" # jsons mapped to LDM
		elif repo == "LEO":
			self.input_folder = "Mapping_files/json_importation_files/Leopard/json_files_mapped_to_LDM/"
		elif repo == "LUH":
			self.input_folder = "Mapping_files/json_importation_files/LUH/json_files_mapped_to_LDM/"
		elif repo == "OSN":
			self.input_folder = "Mapping_files/json_importation_files/OsnaData/json_files_mapped_to_LDM/"
		self.output_file = outfile

	@staticmethod
	def _strip_newlines(text):
		"""
		Clean text by removing newline characters and stripping whitespace.

		Parameters:
		----------
		text : str
			The input text to be cleaned.

		Returns:
		-------
		str
			The cleaned text with newlines replaced by spaces and stripped of leading/trailing whitespace.
		"""
		return text.replace("\r\n", " ").replace("\n", " ").replace("\r", " ").strip()

	def preprocess_datasets(self):
		"""
		Preprocess dataset files from the specified repository and save the results to an output JSON file.
		This method enriches raw metadata with KG-friendly fields (URLs, ORCID links, cleaned text).

		Returns:
		-------
		list
			A list of preprocessed datasets.
		"""
		input_files = [self.input_folder + file for file in os.listdir(self.input_folder)]
		output_file = self.output_file
		data = []
		
		for f in input_files:
			with open(f, "r", encoding="utf-8") as file:
				data_aux = json.load(file)
				row=data_aux
						# print(row)
				url = f"{self.kg_domain}/{row['name']}"
				row['kg_domain'] = self.kg_domain

				if row.get('orcid'):
					row['orcid'] = "https://orcid.org/" + row['orcid']

				for field in ("authors", "resources", "tags"):
					for sub_row in row.get(field, []):
						if field == "resources":
							sub_row["data_id"] = row["name"]
							if not sub_row.get('size'):
								sub_row['size'] = ''
							if 'description' in sub_row:
								sub_row['description'] = self._strip_newlines(sub_row['description'])
						elif field == "tags":
							sub_row["data_id"] = row["name"]
						elif field == "authors" and sub_row.get('orcid'):
							sub_row['orcid'] = "https://orcid.org/" + sub_row['orcid']

						sub_row['url'] = url
						sub_row['kg_domain'] = self.kg_domain

				if row.get('notes'):
					row['notes'] = self._strip_newlines(row['notes'])
			
			data.append(data_aux)

		with open(output_file, "w", encoding="utf-8") as file:
			json.dump(data, file, indent=2)

		print(f"Preprocessed {len(data)} datasets and saved to '{output_file}'")
		return data

if __name__ == "__main__":
	if len(sys.argv) == 1:
		exit("Need at least one argument:\tWhich repo to parse dataset files from (GOE, LEO, LUH, OSN)?\nOptional second argument:\tOutput file path (default: process-validation/importation-process/preprocessed-datasets/<repo>.json)")
	elif len(sys.argv) == 2:
		repo = sys.argv[1]
		outfile=f"process-validation/importation-process/preprocessed-datasets/{repo}.json"
	elif len(sys.argv) > 2:
		repo = sys.argv[1]
		outfile = sys.argv[2]

	kg = KG_creation(repo, outfile)
	kg.preprocess_datasets()