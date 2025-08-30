# Boston House Pricing Prediction

## Software and Tools Required

1. [Github Account](https://github.com)
2. [Heroku Account](https://heroku.com)
3. [VS Code IDE](https://code.visualstudio.com)
4. [Git CLI](https://git-scm.com)

## Project Overview

This project uses linear regression algorithm to predict house prices based on various features from the Boston housing dataset. It includes data preprocessing, exploratory data analysis, model training, evaluation, and deployment instructions.

## Setup Instructions

1. Clone the repository:
	```bash
	git clone https://github.com/iamjunaidjutt/boston_house_pricing.git
	```
2. Navigate to the project directory:
	```bash
	cd boston_house_pricing
	```
3. Create a new environment:


3. Create a new Python environment (recommended):
	 - Using venv (standard Python):
		 ```bash
		 python -m venv venv
		 source venv/bin/activate  # On Windows use: venv\Scripts\activate
		 ```
	 - Or using conda:
		 ```bash
		 conda create -n boston_env python=3.10
		 conda activate boston_env
		 ```

4. Install required Python packages:
	 ```bash
	 pip install -r requirements.txt
	 ```

## Usage

1. Run the Jupyter notebook to explore the analysis and model training steps:
	```bash
	jupyter notebook
	```
2. For deployment, follow the instructions in the deployment section of the notebook or documentation.

## Deployment

You can deploy the Flask API and Next.js frontend to Heroku, Vercel, or other cloud platforms. See the `Procfile` and deployment instructions in the repository for details.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the Apache License 2.0.

## Contact

For questions or feedback, contact [iamjunaidjutt](https://github.com/iamjunaidjutt).