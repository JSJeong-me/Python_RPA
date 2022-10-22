{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO792s1VA1QNaWC/KZG3RUr",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/JSJeong-me/Python_RPA/blob/main/Robot_framework/task.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "LK_RVWQiStPW"
      },
      "outputs": [],
      "source": [
        "# Robot to enter weekly sales data into the RobotSpareBin Industries Intranet.\n",
        "# https://robocorp.com/docs/courses/beginners-course/python-robot\n",
        "\n",
        "import os\n",
        "\n",
        "from Browser import Browser\n",
        "from Browser.utils.data_types import SelectAttribute\n",
        "from RPA.Excel.Files import Files\n",
        "from RPA.HTTP import HTTP\n",
        "from RPA.PDF import PDF\n",
        "\n",
        "\n",
        "browser = Browser()\n",
        "\n",
        "\n",
        "def open_the_intranet_website():\n",
        "    browser.new_page(\"https://robotsparebinindustries.com/\")\n",
        "\n",
        "\n",
        "def log_in():\n",
        "    browser.type_text(\"css=#username\", \"maria\")\n",
        "    browser.type_secret(\"css=#password\", \"thoushallnotpass\")\n",
        "    browser.click(\"text=Log in\")\n",
        "\n",
        "\n",
        "def download_the_excel_file():\n",
        "    http = HTTP()\n",
        "    http.download(\n",
        "        url=\"https://robotsparebinindustries.com/SalesData.xlsx\",\n",
        "        overwrite=True)\n",
        "\n",
        "\n",
        "def fill_and_submit_the_form_for_one_person(sales_rep):\n",
        "    browser.type_text(\"css=#firstname\", sales_rep[\"First Name\"])\n",
        "    browser.type_text(\"css=#lastname\", sales_rep[\"Last Name\"])\n",
        "    browser.type_text(\"css=#salesresult\", str(sales_rep[\"Sales\"]))\n",
        "    browser.select_options_by(\n",
        "        \"css=#salestarget\",\n",
        "        SelectAttribute[\"value\"],\n",
        "        str(sales_rep[\"Sales Target\"]))\n",
        "    browser.click(\"text=Submit\")\n",
        "\n",
        "\n",
        "def fill_the_form_using_the_data_from_the_excel_file():\n",
        "    excel = Files()\n",
        "    excel.open_workbook(\"SalesData.xlsx\")\n",
        "    sales_reps = excel.read_worksheet_as_table(header=True)\n",
        "    excel.close_workbook()\n",
        "    for sales_rep in sales_reps:\n",
        "        fill_and_submit_the_form_for_one_person(sales_rep)\n",
        "\n",
        "\n",
        "def collect_the_results():\n",
        "    browser.take_screenshot(\n",
        "        filename=f\"{os.getcwd()}/output/sales_summary.png\",\n",
        "        selector=\"css=div.sales-summary\")\n",
        "\n",
        "\n",
        "def export_the_table_as_a_pdf():\n",
        "    sales_results_html = browser.get_property(\n",
        "        selector=\"css=#sales-results\", property=\"outerHTML\")\n",
        "    pdf = PDF()\n",
        "    pdf.html_to_pdf(sales_results_html, \"output/sales_results.pdf\")\n",
        "\n",
        "\n",
        "def log_out():\n",
        "    browser.click(\"text=Log out\")\n",
        "\n",
        "\n",
        "def main():\n",
        "    try:\n",
        "        open_the_intranet_website()\n",
        "        log_in()\n",
        "        download_the_excel_file()\n",
        "        fill_the_form_using_the_data_from_the_excel_file()\n",
        "        collect_the_results()\n",
        "        export_the_table_as_a_pdf()\n",
        "    finally:\n",
        "        log_out()\n",
        "        browser.playwright.close()\n",
        "\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ]
    }
  ]
}