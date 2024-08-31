1.Research and Target Industry Identification:
Concluded that Tech Recruiting company would likely be interested in companies within the tech industry


2.NACE Code Selection:
Identified and selected the following NACE codes related to the tech industry:
6201, 6202, 6203, 6209, 2611, 2612, 2620, 2630, 5821, 5829, 6311, 6312, 7219


3.Data Processing and Analysis (using Python with Pandas, numpy):
3.1 Initial Filtering
- Filtered companies based on selected NACE codes
- Reduced dataset from 22,000+ to approximately 1,600 tech-related companies

3.2 Data Normalization
- Normalized values for the following columns:
* Taxable turnover 2019
* Taxable turnover 2020Q1, Q2, Q3
* National taxes 2020Q3
* Labour taxes 2020Q3
* Employee count 2020Q3
* Debt (treated as a negative value)

3.3 Ranking and Selection:
- Summed up normalized values for each company
- Sorted list in descending order based on total scores
- Selected top 400 companies based on this ranking

4.Output Generation:
4.1 Original File Modification
- Highlighted selected 300 companies in the original file
- Maintained integrity of all other data

4.2 Additional Output
- Created a separate file with the sorted list of chosen companies

Conclusion:
This methodology provides a data-driven approach to identifying the
 most financially stable and promising tech companies from the given dataset.
 The process ensures a balanced consideration of various financial indicators while 
focusing on the relevant industry sector.
