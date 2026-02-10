# Project Folder Structure

```
README.md
ai_engine/
	__init__.py
	requirements.txt
	__pycache__/
	demand_forecasting/
		__init__.py
		features.py
		model.py
		train.py
		__pycache__/
	route_eta/
		features.py
		model.py
		train.py
		__pycache__/
	utils/
		encoders.py

backend/
	requirements.txt
	app/
		__iniit__.py
		create_tables.py
		main.py
		__pycache__/
		api/
			__init__.py
			demand.py
			health.py
			shipping.py
			__pycache__/
		core/
			__init__.py
			config.py
			database.py
			__pycache__/
		models/
			__init__.py
			order.py
			shipment.py
			__pycache__/
		schemas/
			__init__.py
			demand.py
			shipping.py
			__pycache__/

data/
	processed/
	raw/
	samples/

docker/
	ai.Dockerfile
	backend.Dockerfile

frontend/
	streamlit_app/
		app.py
		requirements.txt

notebooks/
	exploration.ipynb
vectore_index/
	faiss_index/
```
