{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Max Temperature is : 50\n",
      "Days of rain : ['1/9/2016', '1/10/2016', '1/16/2016', '1/27/2016']\n",
      "Average wind speed is : 6.0\n"
     ]
    }
   ],
   "source": [
    "_parsed_rows = []\n",
    "\n",
    "def parse_csv():\n",
    "    import csv\n",
    "    _file_path = \"../nyc_weather.csv\"\n",
    "\n",
    "    global _parsed_rows\n",
    "    with open(_file_path, \"r\") as f:\n",
    "        reader = csv.reader(f, delimiter=',')\n",
    "        reader.next()\n",
    "        for row in reader:\n",
    "            _parsed_rows.append({\n",
    "                'date':  row[0],\n",
    "                'temperature': row[1],\n",
    "                'DewPoint': row[2],\n",
    "                'Humidity': row[3],\n",
    "                'Sea_Level_PressureIn': row[4],\n",
    "                'VisibilityMiles': row[5],\n",
    "                'WindSpeedMPH': row[6],\n",
    "                'PrecipitationIn': row[7],\n",
    "                'CloudCover': row[8],\n",
    "                'Events': row[9],\n",
    "                'WindDirDegrees': row[10]\n",
    "            })\n",
    "            \n",
    "def get_max_temperature():\n",
    "    max_temp = 0\n",
    "    for row in _parsed_rows:\n",
    "        if int(row['temperature']) > max_temp:\n",
    "            max_temp = int(row['temperature'])\n",
    "    return max_temp\n",
    "\n",
    "def get_days_of_rain(event):\n",
    "    days = []\n",
    "    for row in _parsed_rows:\n",
    "        if row['Events'] == event:\n",
    "            days.append(row['date'])\n",
    "    return days\n",
    "\n",
    "def get_avg_wind_speed():\n",
    "    total = 0\n",
    "    count = 0\n",
    "    for row in _parsed_rows:\n",
    "        speed = 0 if row['WindSpeedMPH']=='' else int(row['WindSpeedMPH'])\n",
    "        total += speed\n",
    "        count += 1\n",
    "    return float(total/count)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    parse_csv()\n",
    "    \n",
    "    print \"Max Temperature is : \" + str(get_max_temperature())\n",
    "    print \"Days of rain : \" + str(get_days_of_rain('Rain'))\n",
    "    print \"Average wind speed is : \" + str(get_avg_wind_speed())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
