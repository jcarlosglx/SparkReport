# API Template

The main idea of the project is to have a reporting tool where Apache Spark is the information manager. For the present
example I use a "database" with stocks (don't use it for real)

## Aim

At present, information is valuable, but it is only unpredictable when we understand the impact that we can generate 
either with a product or service. So having a tool that can synthesize the above through reports can, among many other 
things: add value to decision-making, simplify a sea of data, save time and effort.

## Features

- GET, data endpoints
  * localhost/api/single
    * This will give a report with a single graphic (for specialized analysis) and if you wish a set of statistics
  * localhost/api/quarter
      * This will give a report with up to for graphic and if you wish a set of statistics
  * localhost/api/square
      * This will give a report with up to six graphic but no set of statistics
- Analysis
    * Graphics
        * For the moment we can handle the next graphics
          * Histogram
          * BoxPlot
          * MultiBoxPlot
          * Plot
          * MultiPlot
          * Scatter
  * Non Graphics
      * For the moment we can handle the next non graphics
          * Min
          * Max
          * Mean
          * Mode
          * Median
          * Standard Deviation
- A Middleware for create and save logs
- Security in the processing of the data
- A set of commands for repetitive tasks for example: testing, create/delete db, CI/CD, etc.
- A Dockerfile for test/dev
- A Kubernetes configuration for test/dev

## Usage
### User

To interact with the program ask HTTP's request type GET with the JSON in the next way

JSON = {
    "Graphics" : [\'Histogram\'],
    "NonGraphics" : [\'Statistics\'],
    "y" : [\'AAPL\'],
    "x" : [\'Date\']
}
Since all params are list, you send more than one, and of course you will receive each graphic with the params
#### Optionals params:
- Graphics
  * Histogram
  * BoxPlot
  * MultiBoxPlot
  * Plot
  * MultiPlot
  * Scatter
- NonGraphics
    * Statistics 
- y
  * Date 
  * AAPL 
  * T 
  * BA 
  * MGM 
  * IBM 
  * TSLA 
  * GOOG
  * sp500
#### Required params:
- x
    * Date 
    * AAPL 
    * T 
    * BA 
    * MGM 
    * IBM 
    * TSLA 
    * GOOG
    * sp500

### Developer

- If you are a developer there is a folder called app/commands where you can find a set
of commands for save time

### DevOps

- If you are a DevOps person there is a Makefile where it can help you with the CD/CI

## Technologies

### Some of the technologies used:

- API-REST
- Python
- Spark
- Flask
- Pytest
- Docker
- Kubernetes
- Gunicorn
- Processing management