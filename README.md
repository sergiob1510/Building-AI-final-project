# Predicting yield in agriculture with AI

The Building AI course is focused on solving real world problems using AI methods. The point is: how can we deal with daily problems in a more efficient and innovative way using computers?

There are many ways to achieve this. The potential of AI is gigantic if we find the correct application for it.

## Summary

The project consists in building a wheat yield predictor using meteorological (ammount of rainfall, mean temperatures and solar radiation) and soil data. Evaluating data collected from last recent years, the program should be able to produce an estimation.

## Background

As world's populations keeps growing, we need to produce larger amounts of food. Big companies are already using large amounts of data collected in their fields to make the right decisions and manage their plantations. The general idea behind this project is to make it possible for small/new farmers to produce accurate calculations too, using Machine Learning models for predictions. This should give them another tool (information) to help them determine their next steps and set up a prosperous business.
Reducing the information gap between big and small farmers is key if we want to stop the concentration of land ownership. We need small farmers, they are the future of food (You can read more on the subject in https://www.ifad.org/en/web/latest/blog/asset/42168286 or https://www.nationalgeographic.com/environment/article/photos-farms-agriculture-national-farmers-day)

# About the program

This is just a snippet of what could be done. I made it work only for wheat and for Argentina. A good predictor should include larger amounts of data from different regions, even countries, to become more accurate and make better predictions. Also, it should be made for other crops if we want to build something really useful.

## How is it used?

The user must fill the required data and then the prediction is made, using the coefficients calculated by statistical data collected from that region/country in particular.


## Data sources and AI methods

The data used for this little demo comes from government sources:

* Anual yield - [Ministry of Agriculture - http://datosestimaciones.magyp.gob.ar/reportes.php?reporte=Estimaciones]
* Climate statistics
	** Buenos Aires: [National Meteorological Service - http://www3.smn.gob.ar/]
	** Tucuman: [Agroindustrial Experimental Station "Obispo Colombres" - https://agromet.eeaoc.gob.ar/graficos.php?estacn=2049&desde=01%2F01%2F2021&hasta=05%2F03%2F2021&opcion=1]
	** Chaco: [National Meteorological Service - http://www3.smn.gob.ar/]
* Solar energy statistics - [RIGHINI, Raúl; GROSSI GALLEGOS, Hugo - Mapa de energía solar colectada anualmente por un plano inclinado. Un ángulo óptimo en la República Argentina. Cuarto Congreso Nacional de Hidrógeno y Fuentes Sustentables de Energía, 2011]
* Soil quality (Organic CO and pH): [AA.VV - Guía para la evaluación de la calidad de los suelos de textura fina bajo agricultura en siembra directa en Chaco subhúmedo, en áreas sujetas a cambios en el uso del suelo, INTA], [SAINZ ROZAS, Hernán, ECHEVERRIA, Hernán y ANGELINI, Hernán - Niveles de materia orgánica y pH en suelos agrícolas de la región pampeana y extrapampeana argentina. Informaciones Agronómicas No 2, International Plant Nutrition Institute]

* Method used: Linear regression with Python and NumPy.

## Challenges

* This project doesn't include external variables -political, socio-economic- that could influence in the results. Remember, it's just a small demo.
* To make it work, data cleansing is mandatory. Even with the tiny amount of data used, I came across dubious statistics and had to do a lot of cleaning.
* Natural disasters -floods, droughts, fires, etc- are not held into account but they can affect output.


## What next?

To make this grow and become really useful, the project needs technical assistance from experts in the area: agricultural engineers. They can suggest variables to add, sources for the data needed, etc. 


## Acknowledgments

* University of Helsinki for making the course available
* Reaktor for pairing up with the University of Helsinki to make this course
* Everyone in the Elements of AI Spectrum community

If you've found this useful or have any doubts, please contact me: sergio15bianco@gmail.com
