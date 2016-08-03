..  Copyright (C)  Brad Miller, David Ranum, Jeffrey Elkner, Peter Wentworth, Allen B. Downey, Chris
    Meyers, and Dario Mitchell.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, Prefaces, and
    Contributor List, no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".


.. setup for automatic question numbering.

.. 	qnum::
	:start: 1
	:prefix: 18-10-

Chapter 18 Exercises
---------------------

Here are just the first 9 lines of the data for city pollution. The data is in the order: City, PM 10, PM 2.5. This data set will be used for exercise questions 1 - 12.

 ::

     Aberdeen, SD :13 :8
     Adrian, MI :15 :9
     Akron, OH :18 :11
     Albany, GA :18 :11
     Albany-Lebanon, OR :14 :8
     Albany-Schenectady-Troy, NY :13 :8
     Albuquerque, NM :12 :7
     Alexandria, LA :20 :12

If you want to see **all** of the data click on the *Show* button below.  Once it appears, you can hide it again by clicking on the *Hide* button.

.. reveal:: pol_Data1
    :showtitle: Show
    :hidetitle: Hide

    .. raw:: html

       <pre id="uspoll.txt">
       Aberdeen, SD :13 :8
       Adrian, MI :15 :9
       Akron, OH :18 :11
       Albany, GA :18 :11
       Albany-Lebanon, OR :14 :8
       Albany-Schenectady-Troy, NY :13 :8
       Albuquerque, NM :12 :7
       Alexandria, LA :20 :12
       Allegan, MI :14 :9
       Allentown-Bethlehem-Easton, PA-NJ :21 :12
       Altoona, PA :19 :12
       Anchorage, AK :13 :8
       Anderson, IN :18 :11
       Ann Arbor, MI :16 :10
       Appleton, WI :14 :9
       Asheville, NC :15 :9
       Athens, OH :14 :9
       Athens, TN :15 :9
       Athens-Clarke County, GA :16 :9
       Atlanta-Sandy Springs-Marietta, GA :23 :14
       Atlantic City-Hammonton, NJ :14 :8
       Augusta-Richmond County, GA-SC :18 :11
       Augusta-Waterville, ME :14 :9
       Austin-Round Rock, TX :17 :10
       Bakersfield, CA :24 :15
       Baltimore-Towson, MD :20 :12
       Bangor, ME :12 :7
       Baraboo, WI :17 :10
       Baton Rouge, LA :19 :11
       Bay City, MI :13 :8
       Beaver Dam, WI :15 :9
       Beckley, WV :14 :8
       Bellingham, WA :7 :4
       Bennington, VT :11 :7
       Birmingham-Hoover, AL :20 :12
       Bishop, CA :11 :6
       Bismarck, ND :11 :6
       Bloomington, IN :17 :10
       Bloomington-Normal, IL :16 :9
       Boise City-Nampa, ID :17 :10
       Boone, NC :13 :8
       Boston-Cambridge-Quincy, MA-NH :16 :10
       Boulder, CO :12 :7
       Bowling Green, KY :17 :10
       Bradenton-Sarasota-Venice, FL :12 :7
       Brainerd, MN :8 :5
       Bremerton-Silverdale, WA :7 :4
       Bridgeport-Stamford-Norwalk, CT :16 :9
       Brigham City, UT :12 :7
       Brookings, SD :14 :9
       Brownsville-Harlingen, TX :16 :10
       Brunswick, GA :13 :8
       Buffalo-Niagara Falls, NY :16 :9
       Burlington, NC :14 :9
       Burlington-South Burlington, VT :12 :7
       Butte-Silver Bow, MT :19 :11
       Cadillac, MI :10 :6
       Cambridge, MD :13 :8
       Canton-Massillon, OH :21 :12
       Cape Coral-Fort Myers, FL :12 :7
       Casper, WY :9 :5
       Cedar Rapids, IA :16 :10
       Champaign-Urbana, IL :16 :10
       Charleston, WV :18 :11
       Charleston-North Charleston-Summerville, SC :16 :10
       Charlotte-Gastonia-Concord, NC-SC :16 :10
       Charlottesville, VA :13 :8
       Chattanooga, TN-GA :18 :11
       Cheyenne, WY :9 :6
       Chicago-Naperville-Joliet, IL-IN-WI :22 :13
       Chico, CA :12 :7
       Cincinnati-Middletown, OH-KY-IN :23 :14
       Clarksburg, WV :16 :10
       Clarksville, TN-KY :16 :10
       Clearlake, CA :7 :4
       Cleveland-Elyria-Mentor, OH :24 :15
       Clinton, IA :18 :11
       Colorado Springs, CO :12 :7
       Columbia, SC :17 :10
       Columbia, TN :14 :8
       Columbus, GA-AL :19 :11
       Columbus, OH :18 :11
       Concord, NH :16 :9
       Cookeville, TN :14 :9
       Corning, NY :11 :7
       Corpus Christi, TX :18 :11
       Dallas-Fort Worth-Arlington, TX :20 :12
       Daphne-Fairhope-Foley, AL :15 :9
       Davenport-Moline-Rock Island, IA-IL :18 :11
       Dayton, OH :18 :11
       Decatur, AL :15 :9
       Decatur, IL :17 :10
       Deltona-Daytona Beach-Ormond Beach, FL :11 :6
       Denver-Aurora-Broomfield, CO :14 :9
       Des Moines-West Des Moines, IA :15 :9
       Detroit-Warren-Livonia, MI :21 :12
       Dickinson, ND :7 :4
       Dothan, AL :15 :9
       Dover, DE :14 :8
       Duluth, MN-WI :11 :6
       Durango, CO :7 :4
       Durham, NC :14 :8
       Durham-Chapel Hill, NC :14 :8
       Dyersburg, TN :15 :9
       East Stroudsburg, PA :13 :8
       Eau Claire, WI :14 :8
       El Centro, CA :24 :14
       El Dorado, AR :18 :11
       El Paso, TX :21 :12
       Elizabethtown, KY :20 :12
       Elkhart-Goshen, IN :21 :12
       Erie, PA :19 :11
       Eugene-Springfield, OR :13 :8
       Eureka-Arcata-Fortuna, CA :11 :7
       Evansville, IN-KY :19 :12
       Fairbanks, AK :31 :19
       Fairmont, WV :17 :10
       Fargo, ND-MN :13 :8
       Farmington, NM :8 :5
       Fayetteville, NC :15 :9
       Fayetteville-Springdale-Rogers, AR-MO :16 :10
       Flagstaff, AZ :9 :5
       Flint, MI :13 :8
       Florence, SC :15 :9
       Florence-Muscle Shoals, AL :15 :9
       Fort Collins-Loveland, CO :12 :7
       Fort Madison-Keokuk, IA-MO :18 :11
       Fort Payne, AL :15 :9
       Fort Smith, AR-OK :17 :10
       Fort Wayne, IN :23 :14
       Fresno, CA :74 :45
       Gadsden, AL :16 :10
       Gainesville, FL :12 :7
       Gainesville, GA :16 :9
       Gettysburg, PA :18 :11
       Gillette, WY :13 :8
       Goldsboro, NC :21 :13
       Grand Island, NE :13 :8
       Grand Junction, CO :12 :7
       Grand Rapids-Wyoming, MI :16 :10
       Grants Pass, OR :12 :7
       Greeley, CO :13 :8
       Green Bay, WI :16 :10
       Greensboro-High Point, NC :14 :9
       Greenville, NC :13 :8
       Greenville-Mauldin-Easley, SC :16 :10
       Grenada, MS :16 :9
       Gulfport-Biloxi, MS :16 :10
       Hagerstown-Martinsburg, MD-WV :19 :11
       Hammond, LA :15 :9
       Hanford-Corcoran, CA :28 :17
       Harriman, TN :22 :13
       Harrisburg-Carlisle, PA :20 :12
       Harrisonburg, VA :15 :9
       Hartford-West Hartford-East Hartford, CT :14 :9
       Hattiesburg, MS :18 :11
       Helena, MT :16 :9
       Helena-West Helena, AR :16 :9
       Hickory-Lenoir-Morganton, NC :16 :10
       Hilo, HI :27 :16
       Hobbs, NM :13 :8
       Holland-Grand Haven, MI :15 :9
       Homosassa Springs, FL :11 :7
       Honolulu, HI :12 :7
       Hot Springs, AR :18 :11
       Houma-Bayou Cane-Thibodaux, LA :13 :8
       Houston-Sugar Land-Baytown, TX :21 :13
       Huntington-Ashland, WV-KY-OH :19 :11
       Huntsville, AL :16 :9
       Indianapolis-Carmel, IN :25 :15
       Iowa City, IA :16 :10
       Jackson, MS :19 :11
       Jackson, TN :15 :9
       Jackson, WY-ID :11 :6
       Jacksonville, FL :13 :8
       Jamestown-Dunkirk-Fredonia, NY :13 :8
       Jasper, IN :18 :11
       Johnstown, PA :19 :12
       Juneau, AK :11 :6
       Kahului-Wailuku, HI :11 :6
       Kalamazoo-Portage, MI :17 :10
       Kalispell, MT :13 :8
       Kansas City, MO-KS :24 :15
       Kapaa, HI :11 :7
       Keene, NH :16 :10
       Kingsport-Bristol-Bristol, TN-VA :15 :9
       Kinston, NC :13 :8
       Klamath Falls, OR :18 :11
       Knoxville, TN :18 :11
       Kokomo, IN :16 :10
       La Crosse, WI-MN :14 :8
       Laconia, NH :11 :7
       Lafayette, IN :24 :14
       Lafayette, LA :18 :11
       Lake Charles, LA :14 :8
       Lake Havasu City-Kingman, AZ :6 :4
       Lakeland-Winter Haven, FL :13 :8
       Lancaster, PA :21 :13
       Lansing-East Lansing, MI :14 :9
       Laramie, WY :9 :6
       Las Cruces, NM :25 :15
       Las Vegas-Paradise, NV :20 :12
       Laurel, MS :18 :11
       Lawrenceburg, TN :14 :8
       Lebanon, NH-VT :11 :7
       Lebanon, PA :24 :14
       Lewiston-Auburn, ME :13 :8
       Lexington-Fayette, KY :16 :10
       Lima, OH :17 :10
       Lincoln, NE :14 :9
       Little Rock-North Little Rock-Conway, AR :19 :12
       Logan, UT-ID :15 :9
       Los Angeles-Long Beach-Santa Ana, CA :33 :20
       Louisville/Jefferson County, KY-IN :22 :13
       Lumberton, NC :14 :9
       Lynchburg, VA :13 :8
       Macon, GA :19 :12
       Madera, CA :27 :16
       Madison, WI :16 :9
       Manchester-Nashua, NH :14 :8
       Marshall, MN :12 :7
       Marshall, TX :17 :10
       McAlester, OK :19 :11
       McAllen-Edinburg-Mission, TX :18 :11
       Medford, OR :15 :9
       Memphis, TN-MS-AR :17 :10
       Merced, CA :18 :11
       Meridian, MS :17 :10
       Miami-Fort Lauderdale-Pompano Beach, FL :14 :8
       Michigan City-La Porte, IN :16 :10
       Middlesborough, KY :17 :10
       Milwaukee-Waukesha-West Allis, WI :18 :11
       Minneapolis-St. Paul-Bloomington, MN-WI :17 :10
       Missoula, MT :21 :12
       Mobile, AL :15 :9
       Modesto, CA :25 :15
       Monroe, LA :22 :13
       Monroe, MI :16 :9
       Montgomery, AL :18 :11
       Morgantown, WV :15 :9
       Mount Vernon, IL :14 :9
       Muncie, IN :16 :10
       Muscatine, IA :18 :11
       Muskegon-Norton Shores, MI :15 :9
       Napa, CA :23 :14
       Nashville-Davidson--Murfreesboro--Franklin, TN :17 :10
       New Castle, IN :15 :9
       New Haven-Milford, CT :15 :9
       New Orleans-Metairie-Kenner, LA :21 :13
       New York-Northern New Jersey-Long Island, NY-NJ-PA :23 :14
       Niles-Benton Harbor, MI :14 :9
       Nogales, AZ :16 :10
       Norwich-New London, CT :13 :8
       Ogden-Clearfield, UT :15 :9
       Oklahoma City, OK :16 :10
       Omaha-Council Bluffs, NE-IA :19 :12
       Orlando-Kissimmee, FL :12 :7
       Owensboro, KY :18 :11
       Oxnard-Thousand Oaks-Ventura, CA :16 :10
       Paducah, KY-IL :17 :10
       Palm Bay-Melbourne-Titusville, FL :10 :6
       Parkersburg-Marietta-Vienna, WV-OH :17 :10
       Pascagoula, MS :15 :9
       Pendleton-Hermiston, OR :12 :7
       Pensacola-Ferry Pass-Brent, FL :14 :8
       Peoria, IL :16 :10
       Philadelphia-Camden-Wilmington, PA-NJ-DE-MD :28 :17
       Phoenix-Mesa-Scottsdale, AZ :26 :16
       Pittsburgh, PA :25 :15
       Pittsfield, MA :14 :9
       Platteville, WI :15 :9
       Pocatello, ID :15 :9
       Ponca City, OK :17 :10
       Portland-South Portland-Biddeford, ME :15 :9
       Portland-Vancouver-Beaverton, OR-WA :12 :7
       Portsmouth, OH :16 :10
       Poughkeepsie-Newburgh-Middletown, NY :13 :8
       Prescott, AZ :7 :4
       Prineville, OR :14 :9
       Providence-New Bedford-Fall River, RI-MA :18 :11
       Provo-Orem, UT :14 :8
       Pueblo, CO :11 :7
       Quincy, IL-MO :16 :10
       Raleigh-Cary, NC :16 :9
       Rapid City, SD :11 :6
       Reading, PA :19 :11
       Red Bluff, CA :14 :8
       Redding, CA :10 :6
       Reno-Sparks, NV :15 :9
       Richmond, VA :15 :9
       Richmond-Berea, KY :15 :9
       Riverside-San Bernardino-Ontario, CA :34 :21
       Riverton, WY :13 :8
       Roanoke, VA :15 :9
       Rochester, MN :13 :8
       Rochester, NY :14 :9
       Rock Springs, WY :13 :8
       Rockford, IL :16 :9
       Rocky Mount, NC :13 :8
       Rome, GA :18 :11
       Russellville, AR :14 :9
       Rutland, VT :15 :9
       Sacramento--Arden-Arcade--Roseville, CA :15 :9
       Salinas, CA :10 :6
       Salisbury, NC :16 :9
       Salt Lake City, UT :15 :9
       San Antonio, TX :14 :9
       San Diego-Carlsbad-San Marcos, CA :24 :14
       San Francisco-Oakland-Fremont, CA :16 :10
       San Jose-Sunnyvale-Santa Clara, CA :16 :10
       San Luis Obispo-Paso Robles, CA :16 :10
       Santa Barbara-Santa Maria-Goleta, CA :14 :9
       Santa Cruz-Watsonville, CA :10 :6
       Santa Fe, NM :8 :5
       Santa Rosa-Petaluma, CA :14 :8
       Sault Ste. Marie, MI :14 :8
       Savannah, GA :17 :10
       Scottsbluff, NE :9 :6
       Scranton--Wilkes-Barre, PA :14 :8
       Seaford, DE :14 :8
       Seattle-Tacoma-Bellevue, WA :16 :10
       Sheridan, WY :14 :8
       Shreveport-Bossier City, LA :26 :16
       Sierra Vista-Douglas, AZ :11 :7
       Sioux City, IA-NE-SD :16 :10
       Sioux Falls, SD :14 :9
       Somerset, KY :16 :10
       South Bend-Mishawaka, IN-MI :21 :13
       Spartanburg, SC :16 :10
       Spokane, WA :12 :7
       Springfield, IL :16 :10
       Springfield, MA :15 :9
       Springfield, MO :17 :10
       Springfield, OH :17 :10
       St. Cloud, MN :14 :8
       St. George, UT :11 :7
       St. Joseph, MO-KS :20 :12
       St. Louis, MO-IL :22 :13
       State College, PA :19 :11
       Stockton, CA :21 :12
       Syracuse, NY :12 :7
       Talladega-Sylacauga, AL :17 :10
       Tallahassee, FL :14 :9
       Tampa-St. Petersburg-Clearwater, FL :13 :8
       Terre Haute, IN :19 :12
       Texarkana, TX-Texarkana, AR :18 :11
       Thomasville-Lexington, NC :17 :10
       Toledo, OH :17 :10
       Topeka, KS :14 :9
       Torrington, CT :9 :6
       Trenton-Ewing, NJ :15 :9
       Truckee-Grass Valley, CA :10 :6
       Tucson, AZ :10 :6
       Tulsa, OK :16 :10
       Tupelo, MS :16 :10
       Tuscaloosa, AL :16 :9
       Ukiah, CA :12 :7
       Valdosta, GA :14 :9
       Vallejo-Fairfield, CA :15 :9
       Vernal, UT :12 :7
       Virginia Beach-Norfolk-Newport News, VA-NC :14 :8
       Visalia-Porterville, CA :25 :15
       Warner Robins, GA :16 :10
       Washington-Arlington-Alexandria, DC-VA-MD-WV :19 :12
       Waterloo-Cedar Falls, IA :16 :10
       Watertown, SD :18 :11
       Weirton-Steubenville, WV-OH :20 :12
       Wenatchee, WA :17 :10
       Wichita, KS :16 :9
       Wilmington, NC :14 :9
       Winchester, VA-WV :16 :10
       Winston-Salem, NC :15 :9
       Worcester, MA :15 :9
       Yakima, WA :17 :10
       York-Hanover, PA :20 :12
       Youngstown-Warren-Boardman, OH-PA :23 :14
       Yuba City, CA :12 :7
       Yuma, AZ :14 :9
       </pre>

This data set shows the monthly Dow Jones averages from 1989 to 2001. The data is in the order: Date, Open, High, Low, Close, Volume. This data will be used for exercise questions 13 - 20.

::

        3-Dec-01,9848.93,10220.78,9651.87,10021.57
        1-Nov-01,9087.45,10054.58,8987.61,9851.56
        1-Oct-01,8845.97,9626.54,8659.9,9075.14
        4-Sep-01,9946.98,10238.5,7926.93,8847.56
        1-Aug-01,10527.38,10663.07,9829.35,9949.75
        2-Jul-01,10504.95,10758.14,10049.38,10522.81
        1-Jun-01,10913.57,11236.68,10313.4,10502.4
        1-May-01,10734.05,11436.42,10638.48,10911.94
        2-Apr-01,9877.16,10973.15,9303.48,10734.97


If you want to see **all** of the data click on the *Show* button below.  Once it appears, you can hide it again by clicking on the *Hide* button.

.. reveal:: pol_Data1
   :showtitle: Show
   :hidetitle: Hide

   .. raw:: html

      <pre id="stocks.txt">
        3-Dec-01,9848.93,10220.78,9651.87,10021.57
        1-Nov-01,9087.45,10054.58,8987.61,9851.56
        1-Oct-01,8845.97,9626.54,8659.9,9075.14
        4-Sep-01,9946.98,10238.5,7926.93,8847.56
        1-Aug-01,10527.38,10663.07,9829.35,9949.75
        2-Jul-01,10504.95,10758.14,10049.38,10522.81
        1-Jun-01,10913.57,11236.68,10313.4,10502.4
        1-May-01,10734.05,11436.42,10638.48,10911.94
        2-Apr-01,9877.16,10973.15,9303.48,10734.97
        1-Mar-01,10493.25,10940.45,9047.56,9878.78
        1-Feb-01,10884.82,11140.09,10225.14,10495.28
        2-Jan-01,10790.92,11224.41,10325.71,10887.36
        1-Dec-00,10416.76,11044.7,10158.16,10787.99
        1-Nov-00,10966.21,11152.02,10204.8,10414.49
        2-Oct-00,10659.06,11108.79,9571.4,10971.14
        1-Sep-00,11219.54,11518.83,10439.31,10650.92
        1-Aug-00,10523.81,11415.99,10428.58,11215.1
        3-Jul-00,10450.36,10980.34,10303.28,10521.98
        1-Jun-00,10532.27,11013.05,10161.51,10447.89
        1-May-00,10749.42,11086.72,10163.2,10522.33
        3-Apr-00,10863.28,11600.43,10128.62,10733.91
        1-Mar-00,10128.11,11311.28,9611.75,10921.92
        1-Feb-00,10937.74,11228.44,9760.36,10128.31
        3-Jan-00,11501.85,11908.5,10610.43,10940.53
        1-Dec-99,10876.47,11658.68,10798.07,11497.12
        1-Nov-99,10730.78,11195.34,10449.42,10877.81
        1-Oct-99,10335.69,10883.1,9884.2,10729.86
        1-Sep-99,10828.44,11218.39,10055.17,10336.95
        2-Aug-99,10654.83,11428.94,10487.34,10829.28
        1-Jul-99,10972.39,11321.61,10594.99,10655.15
        1-Jun-99,10549.08,11120.24,10334.42,10970.8
        3-May-99,10788.75,11244.36,10372.96,10559.74
        1-Apr-99,9825.29,11072.25,9707.91,10789.04
        1-Mar-99,9315.27,10158.57,9163.41,9786.16
        1-Feb-99,9405.43,9662.77,9025.41,9306.58
        4-Jan-99,9212.84,9759.44,8994.26,9358.83
        1-Dec-98,9039.57,9390.75,8610.63,9181.43
        2-Nov-98,8645.65,9457.95,8573.56,9116.55
        1-Oct-98,7749.42,8718.25,7399.78,8592.1
        1-Sep-98,7583.09,8253.79,7379.7,7842.62
        3-Aug-98,8868.1,8948.17,7517.7,7539.07
        1-Jul-98,9011.56,9412.64,8786.48,8883.29
        1-Jun-98,8907.93,9155.04,8524.55,8952.02
        1-May-98,9106.47,9311.98,8760.95,8899.95
        1-Apr-98,8818.5,9287.32,8715.61,9063.37
        2-Mar-98,8528.78,8997.11,8377.32,8799.81
        2-Feb-98,7987.46,8616.72,7987.46,8545.72
        2-Jan-98,7908.25,8072.91,7391.59,7906.5
        1-Dec-97,7823.62,8209.56,7563.23,7908.25
        3-Nov-97,7443.07,7934.53,7334.77,7823.13
        1-Oct-97,7945.26,8218.34,6936.45,7442.08
        2-Sep-97,7650.99,8078.36,7556.23,7945.26
        1-Aug-97,8222.61,8340.14,7580.85,7622.42
        1-Jul-97,7672.79,8328.99,7613.53,8222.61
        2-Jun-97,7331.04,7868.44,7214.29,7672.79
        1-May-97,7008.99,7430.2,6891.39,7331.04
        1-Apr-97,6583.48,7081.23,6315.84,7008.99
        3-Mar-97,6877.74,7158.28,6532.49,6583.48
        3-Feb-97,6813.09,7112.87,6683.4,6877.74
        2-Jan-97,6448.27,6953.55,6318.96,6813.09
        2-Dec-96,6521.7,6623.96,6206.83,6448.27
        1-Nov-96,6029.38,6606.3,5975.34,6521.7
        1-Oct-96,5882.17,6162.8,5833.72,6029.38
        3-Sep-96,5616.21,5952.08,5550.37,5882.17
        1-Aug-96,5528.91,5761.95,5507.83,5616.21
        1-Jul-96,5654.63,5769.88,5170.11,5528.91
        3-Jun-96,5643.18,5770.61,5559.69,5654.63
        1-May-96,5569.08,5833.04,5327.74,5643.18
        1-Apr-96,5587.14,5737.07,5382.66,5569.08
        1-Mar-96,5485.62,5755.86,5395.3,5587.14
        1-Feb-96,5395.3,5693.36,5319.43,5485.62
        2-Jan-96,5117.12,5433.24,5000.07,5395.3
        1-Dec-95,5074.49,5266.69,5016.68,5117.12
        1-Nov-95,4755.48,5143.13,4719.72,5074.49
        2-Oct-95,4789.08,4845.08,4638.43,4755.48
        1-Sep-95,4610.56,4839.48,4594.71,4789.08
        1-Aug-95,4708.47,4772.56,4552.8,4610.56
        3-Jul-95,4556.1,4767.99,4530.26,4708.47
        1-Jun-95,4465.14,4614.2,4394.59,4556.1
        1-May-95,4321.27,4480.7,4278.73,4465.14
        3-Apr-95,4157.69,4348.94,4129.68,4321.27
        1-Mar-95,4011.05,4213.71,3935.31,4157.69
        1-Feb-95,3843.86,4034.62,3809.21,4011.05
        3-Jan-95,3834.44,3955.56,3794.4,3843.86
        1-Dec-94,3739.23,3882.21,3638.97,3834.44
        1-Nov-94,3908.12,3919.9,3612.05,3739.23
        3-Oct-94,3843.19,3958.25,3736.2,3908.12
        1-Sep-94,3913.42,3972.72,3804.5,3843.19
        1-Aug-94,3764.5,3954.54,3722.41,3913.42
        1-Jul-94,3624.96,3782.63,3611.04,3764.5
        1-Jun-94,3758.37,3839.88,3603.92,3624.96
        2-May-94,3681.69,3788.76,3609.71,3758.37
        4-Apr-94,3633.08,3733.15,3520.8,3681.69
        1-Mar-94,3832.02,3911.78,3544.12,3635.96
        1-Feb-94,3978.36,3998.06,3811.76,3832.02
        3-Jan-94,3754.09,4002.84,3715.24,3978.36
        1-Dec-93,3683.95,3818.92,3673.33,3754.09
        1-Nov-93,3680.59,3749.9,3585.86,3683.95
        1-Oct-93,3555.12,3713.57,3541.71,3680.59
        1-Sep-93,3651.25,3665.5,3501.47,3555.12
        2-Aug-93,3539.47,3681.71,3523.54,3651.25
        1-Jul-93,3516.08,3604.86,3443.28,3539.47
        1-Jun-93,3527.43,3577.25,3445.77,3516.08
        3-May-93,3427.55,3582.23,3402.42,3527.43
        1-Apr-93,3435.11,3499.41,3338.39,3427.55
        1-Mar-93,3370.81,3497.25,3334.07,3435.11
        1-Feb-93,3310.03,3472.94,3262.48,3370.81
        4-Jan-93,3301.11,3338.12,3219.25,3310.03
        1-Dec-92,3305.16,3364.87,3229.79,3301.11
        2-Nov-92,3226.28,3326.51,3176.84,3305.16
        1-Oct-92,3271.66,3291.39,3087.41,3226.28
        1-Sep-92,3257.35,3391.35,3226.55,3271.66
        3-Aug-92,3393.78,3413.23,3200.86,3257.35
        1-Jul-92,3318.52,3414.85,3255.43,3393.78
        1-Jun-92,3396.88,3435.27,3242.32,3318.52
        1-May-92,3359.12,3433.98,3316.64,3396.88
        1-Apr-92,3235.47,3387.97,3141.77,3359.12
        2-Mar-92,3267.67,3318.42,3176.21,3235.47
        3-Feb-92,3223.39,3307.47,3193.42,3267.67
        2-Jan-92,3168.83,3313.51,3119.86,3223.39
        2-Dec-91,2894.68,3204.61,2832.29,3168.83
        1-Nov-91,3069.1,3091.91,2861.14,2894.68
        1-Oct-91,3016.77,3091.01,2925.54,3069.1
        3-Sep-91,3043.6,3066.64,2963.1,3016.77
        1-Aug-91,3024.82,3068.65,2836.31,3043.6
        1-Jul-91,2911.67,3039.58,2897.36,3024.82
        3-Jun-91,3027.5,3057.47,2879.25,2906.75
        1-May-91,2887.87,3044.5,2834.53,3027.5
        1-Apr-91,2913.86,3030.45,2848.51,2887.87
        1-Mar-91,2882.18,3017.82,2829.21,2913.86
        1-Feb-91,2736.39,2955.2,2694.31,2882.18
        2-Jan-91,2633.66,2747.28,2447.03,2736.39
        3-Dec-90,2559.65,2662.62,2534.65,2633.66
        1-Nov-90,2442.33,2581.19,2415.59,2559.65
        1-Oct-90,2452.48,2565.35,2344.31,2442.33
        4-Sep-90,2614.36,2665.35,2367.82,2452.48
        1-Aug-90,2905.2,2931.19,2459.41,2614.36
        2-Jul-90,2880.69,3024.26,2833.17,2905.2
        1-Jun-90,2876.66,2956.93,2821.53,2880.69
        1-May-90,2656.76,2908.21,2651.35,2876.66
        2-Apr-90,2707.21,2793.47,2627.7,2656.76
        1-Mar-90,2627.25,2775,2607.88,2707.21
        1-Feb-90,2590.54,2674.32,2540.99,2627.25
        2-Jan-90,2753.2,2834.04,2513.06,2590.54
        1-Dec-89,2706.27,2784.77,2658.7,2753.2
        1-Nov-89,2645.08,2718.22,2563.11,2706.27
        2-Oct-89,2692.82,2809.08,2496.93,2645.08
        1-Sep-89,2737.27,2768.24,2636.78,2692.82
        1-Aug-89,2660.66,2758.73,2619.71,2737.27
        3-Jul-89,2440.06,2668.25,2431.53,2660.66
        1-Jun-89,2480.15,2544.95,2412.94,2440.06
        1-May-89,2418.8,2521.63,2356.3,2480.15
        3-Apr-89,2293.62,2433.1,2282.07,2418.8
        1-Mar-89,2258.39,2351.07,2234.46,2293.62
        1-Feb-89,2342.32,2369.29,2232.14,2258.39
        3-Jan-89,2168.39,2350.18,2127.14,2342.32
      </pre>


#.

    .. tabbed:: ch18ex1t

        .. tab:: Question

            Fix 5 errors in the code below so that the code runs correctly and prints the pollution for all cities that start with the letter A.

            .. activecode:: ch18ex1q
                :nocodelens:

                inFile = open("uspoll.txt","r)
                line = inFile.readLine()
                while line
                    values = line.split(":")
                    city = values[0]
                    if (city.find("A") == 0):
                        print('City: ' city)
                        print("Pollution values:",values[1],values[2])
                    line = infile.readline()

                inFile.close()

        .. tab:: Answer

            Add a ``"`` before the ``)`` in line 1.  Change line 2 to ``readline`` instead of ``readLine``.  Add a ``:`` at the end of line 3.  Add a ``,`` before ``city`` on line 7.  Change ``infile`` to ``inFile`` on line 9.

            .. activecode:: ch18ex1a
                :nocodelens:

                inFile = open("uspoll.txt","r")
                line = inFile.readline()
                while line:
                    values = line.split(":")
                    city = values[0]
                    if (city.find("A") == 0):
                        print('City: ', city)
                        print("Pollution values:",values[1],values[2])
                    line = inFile.readline()

                inFile.close()


        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch18ex1q

#.

    .. tabbed:: ch18ex2t

        .. tab:: Question

            Fix the errors in the code below so that it prints the average PM values of only the cities that start with "A".

            .. activecode::  ch18ex2q
                :nocodelens:

                inFile = open("uspoll.txt","r")
                lines = inFile.readlines()
                inFile.close()

                total25 = 0
                count = 1.0
                for line in lines:
                    values = line.split(":")
                    new25 = float(values[2])
                    city = values[1]
                    if (city.find("A") == -1):
                        total25 = total25 + new25
                    count = count + 1

                print("Average PM 2.5 value for cities that start with "A" is ", total25/count)

        .. tab:: Answer

            In line 10, ``city`` should equal ``values[0]``. In line 11, it should be ``0`` not ``-1``. Indent the count so it is in the body of the if statement.

            .. activecode::  ch18ex2a
                :nocodelens:

                inFile = open("uspoll.txt","r")
                lines = inFile.readlines()
                inFile.close()

                total25 = 0
                count = 1.0
                for line in lines:
                    values = line.split(":")
                    new25 = float(values[2])
                    city = values[0]
                    if (city.find("A") == 0):
                        total25 = total25 + new25
                        count = count + 1

                print("Average PM 2.5 value for cities that start with "A" is ", total25/count)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex2q

#.

    .. tabbed:: ch18ex3t

        .. tab:: Question

           Fix the 5 errors in the code below so that it runs and prints the largest PM 2.5 value and the city that has that value.

           .. activecode::  ch18ex3q
                :nocodelens:

                inFile = open("uspoll.txt","r"
                lines = inFile.readlines()
                inFile.Close()

                maxCity = ''
                max25 =   # initialize max25
                for line  lines:
                    values = line.split(":")
                    new25 = float(values[2]) # get the current value
                    if new25 > max25
                        maxCity = values[0]
                        max25 = new25 # save the new maximum
                print("Largest PM 2.5 value is ",max25," in ",maxCity)


        .. tab:: Answer

            Add a ``)`` at the end of line 1.  Change line 3 to ``close``.  Set ``max25`` to ``0`` in line 6.  Add ``in`` on line 7 before ``lines``.  Add ``:`` at the end of line 10.

            .. activecode::  ch18ex3a
                :nocodelens:

                inFile = open("uspoll.txt","r")
                lines = inFile.readlines()
                inFile.close()

                maxCity = ''
                max25 = 0 # initialize max25
                for line in lines:
                    values = line.split(":")
                    new25 = float(values[2]) # get the current value
                    if new25 > max25:
                        maxCity = values[0]
                        max25 = new25 # save the new maximum
                print("Largest PM 2.5 value is ",max25," in ",maxCity)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex3q

#.

    .. tabbed:: ch18ex4t

        .. tab:: Question

            The code below prints all the lines that have a city that starts with an "A". Change it so that it prints out all lines that have a city that starts with "A" or "B".

            .. activecode::  ch18ex4q
                :nocodelens:

                # read all the lines
                inFile = open("uspoll.txt","r")
                lines = inFile.readlines()
                inFile.close()

                # loop through the lines
                for line in lines:
                    if line[0] == "A":
                        print(line)


        .. tab:: Answer

            Add  an ``or`` clause or an ``elif``.

            .. activecode::  ch18ex4a
                :nocodelens:

                # read all the lines
                inFile = open("uspoll.txt","r")
                lines = inFile.readlines()
                inFile.close()

                # loop through the lines
                for line in lines:
                    if line[0] == "A" or line[0] == "B":
                        print(line)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex4q

#.

    .. tabbed:: ch18ex5t

        .. tab:: Question

           Fix the indention below for the code to correctly find and print the lowest 2.5 value and city.

           .. activecode::  ch18ex5q
                :nocodelens:

                inFile = open("uspoll.txt","r")
                lines = inFile.readlines()
                inFile.close()

                minCity = ''
                min25 = 500
                for line in lines:
                values = line.split(":")
                new25 = float(values[2]) # set the value for new25 to be the current PM 2.5 value
                if new25 < min25:
                minCity = values[0] # Save the minimum city and state
                min25 = new25 # save the minimum PM 2.5 value
                print("Smallest PM 2.5 ",min25," in ",minCity)

        .. tab:: Answer

            Indent lines 8 through 12 as shown below.

            .. activecode::  ch18ex5a
                :nocodelens:

                inFile = open("uspoll.txt","r")
                lines = inFile.readlines()
                inFile.close()

                minCity = ''
                min25 = 500
                for line in lines:
                    values = line.split(":")
                    new25 = float(values[2]) # set the value for new25 to be the current PM 2.5 value
                    if new25 < min25:
                        minCity = values[0] # Save the minimum city and state
                        min25 = new25 # save the minimum PM 2.5 value
                print("Smallest PM 2.5 ",min25," in ",minCity)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex5q

#.

    .. tabbed:: ch18ex6t

        .. tab:: Question

            Fix the code so that it prints out the min value and the cities only when the min value is even.

            .. activecode::  ch18ex6q
                :nocodelens:

                # read all the lines
                inFile = open("uspoll.txt", r)
                lines = inFile.readline
                inFile.close()

                # loop through the lines
                for line in lines:

                    # split at :
                    values = line.split(" ")

                    # get the min PM 2.5 pollution and the city
                    num = str(values[2])
                    city = values[0]

                    # check if even
                    if num % 2 == 0:

                    # print the values
                    print("Even min PM 2.5 ", num ," in ", city)

        .. tab:: Answer

            On line 2, put the "r" in quotations. On line 3, change ``readline`` to ``readlines()``. On line 10, split on the ":" not a space. On the last line, indent the print statement to be in the body of the if clause.

            .. activecode::  ch18ex6a
                :nocodelens:

                # read all the lines
                inFile = open("uspoll.txt","r")
                lines = inFile.readlines()
                inFile.close()

                # loop through the lines
                for line in lines:

                    # split at :
                    values = line.split(":")

                    # get the min PM 2.5 pollution and the city
                    num = float(values[2])
                    city = values[0]

                    # check if even
                    if num % 2 == 0:

                        # print the values
                        print("Even min PM 2.5 ", num ," in ", city)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex6q

#.

    .. tabbed:: ch18ex7t

        .. tab:: Question

           Fix the indention on the lines below so that it correctly prints the average PM 2.5 value.

           .. activecode::  ch18ex7q
                :nocodelens:

                inFile = open("uspoll.txt","r")
                lines = inFile.readlines()
                inFile.close()

                total25 = 0
                count = 1.0
                for line in lines:
                values = line.split(":")
                new25 = float(values[2])
                total25 = total25 + new25
                count = count + 1

                print("Average PM 2.5 value is ",total25/count)

        .. tab:: Answer

            Fix the indention on lines 8-11 as shown below.

            .. activecode::  ch18ex7a
                :nocodelens:

                inFile = open("uspoll.txt","r")
                lines = inFile.readlines()
                inFile.close()

                total25 = 0
                count = 1.0
                for line in lines:
                    values = line.split(":")
                    new25 = float(values[2])
                    total25 = total25 + new25
                    count = count + 1

                print("Average PM 2.5 value is ",total25/count)

        .. tab:: Discussion

            .. disqus::
                :shortname: cslearn4u
                :identifier: teachercsp_ch18ex7q

#.

    .. tabbed:: ch18ex8t

        .. tab:: Question

            Write a procedure that takes in the file name as a parameter and prints out all the cities that start with a vowel (a,e,i,o, or u) and their associated pollution values.

            .. activecode::  ch18ex8q
                :nocodelens:

        .. tab:: Answer

            Define a procedure like shown below

            .. activecode::  ch18ex8a
                :nocodelens:

                def vowelFinder(file):
                    inFile = open(file,"r")
                    line = inFile.readline()
                    while line:
                        values = line.split(":")
                        city = values[0]
                        if (city.find("A") == 0 or city.find("E") == 0):
                            print('City: ', city, "Pollution values:",values[1],values[2])
                        if (city.find("I") == 0 or city.find("O") == 0):
                            print('City: ', city, "Pollution values:",values[1],values[2])
                        if (city.find("U") == 0):
                            print('City: ', city, "Pollution values:",values[1],values[2])

                        line = inFile.readline()

                    inFile.close()

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex8q

#.

    .. tabbed:: ch18ex9t

        .. tab:: Question

           Turn the following code into a procedure.  Pass the input file and the amount of PM 10 to the procedure. It will print the city name and the pollution values for all cities that have that much PM 10 pollution or more.

           .. activecode::  ch18ex9q
                :nocodelens:

                inFile = open("uspoll.txt","r")
                line = inFile.readline()
                while line:
                    values = line.split(":")
                    pollution = float(values[1])
                    if (pollution > 25):
                        print('City: ', values[0])
                        print("Pollution values:",values[1],values[2])
                    line = inFile.readline()

                inFile.close()


        .. tab:: Answer

            Define the procedure as shown below.  Be sure to call the procedure to test it.

            .. activecode::  ch18ex9a
                 :nocodelens:

                 def findPM10GreaterThan(inFile, amount):
                     line = inFile.readline()
                     while line:
                         values = line.split(":")
                         pollution = float(values[1])
                         if (pollution > amount):
                             print('City: ', values[0])
                             print("Pollution values:",values[1],values[2])
                         line = inFile.readline()

                 inFile = open("uspoll.txt","r")
                 findPM10GreaterThan(inFile,25)
                 inFile.close()

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex9q

#.

    .. tabbed:: ch18ex10t

        .. tab:: Question

           Write a function that returns the average PM 2.5 of cities that start with "L".

           .. activecode::  ch18ex10q
                :nocodelens:

        .. tab:: Answer

            Write the function as shown below.

            .. activecode::  ch18ex10a
                :nocodelens:

                def averagePM(file)
                    # read all the lines
                    inFile = open(file,"r")
                    lines = inFile.readlines()
                    inFile.close()
                    sum = 0
                    count = 0
                    # loop through the lines
                    for line in lines:
                        values = line.split(",")
                        if line[0] == "L":
                            pm = float(values[2])
                            sum = sum + pm
                            count += 1
                    return sum / count

                print(averagePM("uspoll.txt"))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex10q

#.

    .. tabbed:: ch18ex11t

        .. tab:: Question

           Change the following code into a procedure that prints the city name and pollution values for all cities that have a PM 2.5 of less than some passed value.  Pass in the input file and the amount of pollution.

           .. activecode::  ch18ex11q
                :nocodelens:

                inFile = open("uspoll.txt","r")
                line = inFile.readline()
                while line:
                    values = line.split(":")
                    pollution = float(values[2])
                    if (pollution < 5):
                        print('City: ', values[0])
                        print("Pollution values:",values[1],values[2])
                    line = inFile.readline()

                inFile.close()


        .. tab:: Answer

            Define a procedure that takes the input file and the amount.  Print all the cities that have lower than the passed amount for PM 2.5.

            .. activecode::  ch18ex11a
                :nocodelens:

                def findPM25LessThan(inFile, amount):
                    line = inFile.readline()
                    while line:
                        values = line.split(":")
                        pollution = float(values[2])
                        if (pollution < amount):
                            print('City: ', values[0])
                            print("Pollution values:",values[1],values[2])
                        line = inFile.readline()

                inFile = open("uspoll.txt","r")
                findPM25LessThan(inFile,5)
                inFile.close()

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex11q

#.

    .. tabbed:: ch18ex12t

        .. tab:: Question

           Write a procedure that takes the name of a city and prints the pollution values for that city if it is found.

           .. activecode::  ch18ex12q
                :nocodelens:

        .. tab:: Answer

            Define the procedure and call it.  Be sure to pass the city name to the procedure.

            .. activecode::  ch18ex12a
                :nocodelens

                def printPollution(inFile,cityName):

                    lines = inFile.readlines()

                    for line in lines:
                        values = line.split(":")
                        city = values[0]
                        if (city.find(cityName) == 0):
                            print('City: ', city)
                            print("Pollution values:",values[1],values[2])

                inFile = open("uspoll.txt","r")
                printPollution(inFile, "Albany, GA")
                inFile.close()


        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex12q

#.

    .. tabbed:: ch18ex13t

        .. tab:: Question

            Complete the code at the ``#`` so that it prints out the date with the biggest loss from open to close.

            .. activecode::  ch18ex13q
                :nocodelens:

                def biggestLoss(file):
                    maxLoss = 0
                    lines = file.readlines()
                    for # in lines:
                        values = line.split(#)
                        open = float(values[#])
                        close = float(values[4])
                        dailyLoss = open # close
                        if (dailyLoss # maxLoss):
                            maxLoss = dailyLoss
                            date = values[#]
                    print(date + " loss " + str(maxLoss))

                file = open("stocks.txt", "r")
                biggestLoss(file)

        .. tab:: Answer

            Complete as shown below.

            .. activecode::  ch18ex13a
                :nocodelens:

                def biggestLoss(file):
                    maxLoss = 0
                    lines = file.readlines()
                    for line in lines:
                        values = line.split(",")
                        open = float(values[1])
                        close = float(values[4])
                        dailyLoss = open - close
                        if (dailyLoss > maxLoss):
                            maxLoss = dailyLoss
                            date = values[0]
                    print(date + " loss " + str(maxLoss))

                file = open("stocks.txt", "r")
                biggestLoss(file)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex13q

#.

    .. tabbed:: ch18ex14t

        .. tab:: Question

            Fix the errors below so that the procedure prints all the dates where the Dow Jones gained more than 300 points from open to close.

            .. activecode::  ch18ex14q
                :nocodelens:

                def pointGain(file):
                    lines = file.readlines()
                    for lines in lines:
                    values = line.split()
                    open = str(values[2])
                    close = float(values[4])
                    if (close - open) < 300:
                        print(values[0])
                file = open("stocks.txt", "r")
                pointGain(file)

        .. tab:: Answer

            Fix the indentation of the body of the for loop. Line 3 should be ``line in lines`` instead of ``lines in lines``. Line 4 should be ``split(",")``. Line 5 should be ``float(line[1])``. Line 7 should be ``>``.

            .. activecode::  ch18ex14a
                :nocodelens:

                def pointGain(file):
                    lines = file.readlines()
                    for lines in lines:
                        values = line.split(",")
                        open = float(values[1])
                        close = float(values[4])
                        if (close - open) > 300:
                            print(values[0])
                file = open("stocks.txt", "r")
                pointGain(file)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex14q

#.

    .. tabbed:: ch18ex15t

        .. tab:: Question

            The code currently prints the date that the Dow Jones had the biggest percent loss. Change 2 lines so that it prints the date with the biggest percent gain.

            .. activecode::  ch18ex15q
                :nocodelens:

                file = open("stocks.txt". "r")
                lines = file.readlines()
                maxGain = 100000
                for line in lines:
                    values = line.split(",")
                    open = float(values[1])
                    close = float(values[4])
                    perChange = ((close - open) / open) * 100
                    if perChange < maxGain:
                        maxGain = perChange
                        date = values[0]
                print(date)

        .. tab:: Answer

            Change line 3 to ``0`` and line 9 to ``>``.

            .. activecode::  ch18ex15a
                :nocodelens:

                file = open("stocks.txt". "r")
                lines = file.readlines()
                maxGain = 0
                for line in lines:
                    values = line.split(",")
                    open = float(values[1])
                    close = float(values[4])
                    perChange = ((close - open) / open) * 100
                    if perChange > maxGain:
                        maxGain = perChange
                        date = values[0]
                print(date)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex15q

#.

    .. tabbed:: ch18ex16t

        .. tab:: Question

            The code below prints all the dates and high price for dates that occur on the first day of the month (i.e. January 1, February 1...). Change it so that it prints the date and low price for all the dates that occur in June.

            .. activecode::  ch18ex16q
                :nocodelens:

                file = open("stocks.txt", "r")
                lines = file.readlines()
                for line in lines:
                    values = line.split(",")
                    date = values[0]
                    if date[0] == "1":
                        print(date + " had a high value of " + values[2])

        .. tab:: Answer

            Split the name by the space and find the first letter of the second item in the new list.

            .. activecode::  ch18ex16a
                :nocodelens:

                file = open("stocks.txt", "r")
                lines = file.readlines()
                for line in lines:
                    values = line.split(",")
                    date = values[0]
                    dateParts = date.split("-")
                    month = dateParts[1]
                    if month == "Jun":
                        print(date + "had a high value of " + values[2])

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex16q

#.

    .. tabbed:: ch18ex17t

        .. tab:: Question

            Write a procedure that takes in the stocks file and a string of the last two digits from the years 1989 - 2001 (i.e. "89") and prints the difference between the highest and lowest points of that year.

            .. activecode::  ch18ex17q
                :nocodelens:

        .. tab:: Answer

            Write a procedure like shown below.

            .. activecode::  ch18ex17a
                :nocodelens:

                def pointChange(file, year):
                    file = open(file, "r")
                    lines = file.readlines()
                    max = 0
                    min = 1000000
                    for line in lines:
                        values = line.split(",")
                        dateParts = values[0].split("-")
                        if dateParts[2] == year:
                            high = float(values[2])
                            low = float(values[3])
                            if high > max:
                                max = high
                            if low < min:
                                min = low
                    print(max - min)

                pointChange("stocks.txt", "89")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex17q

#.

    .. tabbed:: ch18ex18t

        .. tab:: Question

            Write a function that takes the stocks file and the abbreviation for a month (i.e. Jan, Feb) as parameters and returns the average value of all the closing prices during that month from all the years given (Hint: Use a counter variable).

            .. activecode::  ch18ex18q
                :nocodelens:

        .. tab:: Answer

            Define a function like below.

            .. activecode::  ch18ex18a
                :nocodelens:

                def monthAvg(file, month):
                    file = open(file, "r")
                    lines = file.readlines()
                    count = 0
                    sum = 0
                    for line in lines:
                        values = line.split(",")
                        dateParts = values[0].split("-")
                        if dateParts[1] == month:
                            close = float(values[4])
                            sum = sum + close
                            count += 1
                    return sum / count

                print(monthAvg)

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex18q

#.

    .. tabbed:: ch18ex19t

        .. tab:: Question

            Write a function that returns the difference between the average of all the gains or breakevens (0 change) and the absolute value of the average of all the losses from open to close.

           .. activecode::  ch18ex19q
               :nocodelens:

        .. tab:: Answer

            Define a function like below.

            .. activecode::  ch18ex19a
                :nocodelens:

                def avgChange(file):
                    lines = file.readlines()
                    gainSum = 0
                    gainCounter = 0
                    lossSum = 0
                    lossCounter = 0
                    for line in lines:
                        values = line.split(",")
                        open = float(values[1])
                        close = float(values[4])
                        change = close - open
                        if change >= 0:
                            gainSum = gainSum + change
                            gainCounter += 1
                        else:
                            change = change * -1
                            lossSum = lossSum + change
                            lossCounter += 1
                    return (gainSum/gainCounter) - (lossSum/lossCounter)

                file = open("stocks.txt", "r")
                print(avgChange(file))

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex19q

#.

    .. tabbed:: ch18ex20t

        .. tab:: Question

            Write a procedure that takes the stock file as a parameter and prints the date, and high to low change price only for the date that had the highest high to low change out of the dates that fall on the first day of the month.

            .. activecode::  ch18ex20q
                :nocodelens:

        .. tab:: Answer

            Define a function like below.

            .. activecode::  ch18ex20a
                :nocodelens:

                def firstDayChange(file):
                    file = open(file, "r")
                    lines = file.readlines()
                    maxChange = 0
                    for line in lines:
                        values = line.split(",")
                        dateParts = values[0].split("-")
                        if dateParts[0] == "1":
                            high = float(values[2])
                            low = float(values[3])
                            change = high - low
                        if change > maxChange:
                            maxChange = change

                    print(values[0] + " had the max change of " + str(maxChange))

                firstDayChange("stocks.txt")

        .. tab:: Discussion

            .. disqus::
                :shortname: teachercsp
                :identifier: teachercsp_ch18ex20q
