# MoonlightingAnalysis

## Introduction
Moonlighting is when individuals take up an additional job or do extra work outside their regular employment. The term originated from the concept that individuals would work under the moonlight to earn extra income. It is increasingly becoming common in various industries and professions.

# Disadvantages

The disadvantages of moonlighting are:

1.Taking on additional work may disrupt the work-life balance, resulting in increased stress and reduced personal time. It may affect an individual’s health and overall well-being.

2.Splitting time, effort, and energy between jobs can impact focus and concentration. It could lead to lower performance in the primary and additional jobs. The decrease in productivity may lead to dissatisfaction from employers or clients.

3.Engaging in multiple jobs can lead to conflicts of interest, mainly if the secondary position competes directly with the primary job or violates its agreements. This practice may compromise confidentiality, intellectual property, or the employer’s interests, straining professional relationships and may even lead to termination.

4.One of the disadvantages of moonlighting is that it may raise ethical and legal issues, mainly if it violates contractual agreements, breaches intellectual property rights, or involves unethical practices. 

# Corporate Moonlighting Analysis

This project aims to detect overlapping work experiences from an Excel file containing employment records. It can be used to identify potential moonlighting in corporate companies.

## Project Description

The script reads an Excel file with columns `Company`, `DOJ` (Date of Joining), and `DOR` (Date of Resigning). It calculates the overlapping periods between all pairs of job experiences and outputs the results.

## Installation Instructions

1. Clone the repository:
    ```sh
    git clone https://github.com/Skybrowsguy/CorporateMoonlightingAnalysis.git
    ```
2. Navigate to the project directory:
    ```sh
    cd CorporateMoonlightingAnalysis
    ```
3. Install the required libraries:
    ```sh
    pip install pandas openpyxl
    ```

## Usage

1. Place your Excel file in the project directory. Ensure it has columns `Company`, `DOJ`, and `DOR`.
2. Update the file path in the script.
3. Run the script:
    ```sh
    python overlap_analysis.py
    ```

## Example

Given an Excel file `Work_Experience.xlsx` with the following data:

| Company      | DOJ             | DOR             |
|--------------|------------------|-----------------|
| Company A    | 15 December 2018 | 20 February 2020|
| Company B    | 20 January 2020  | 31 March 2022   |
| Company C    | 01 March 2019    | 01 January 2021 |
| Company D    | 15 November 2019 | 25 December 2020|

The script will output:
Overlap between Company A and Company B is from 20 January 2020 to 20 February 2020 with a total of 32 days.
Overlap between Company A and Company C is from 01 March 2019 to 20 February 2020 with a total of 357 days.
Overlap between Company A and Company D is from 15 November 2019 to 20 February 2020 with a total of 98 days.
Overlap between Company B and Company C is from 20 January 2020 to 01 January 2021 with a total of 348 days.
Overlap between Company B and Company D is from 20 January 2020 to 25 December 2020 with a total of 341 days.
Overlap between Company C and Company D is from 15 November 2019 to 01 January 2021 with a total of 414 days.

## License

This project is licensed under the MIT License

Copyright (c) 2024 Swapnil Srivastava





