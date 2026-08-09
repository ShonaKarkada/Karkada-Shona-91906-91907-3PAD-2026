# Purpouse - Store the questions that are to be displayed on the question screen, in the main program - this allows for more robustness, and efficiency when adding questions to the code.

# The main program is in a separate file for increased organisation, maintainability, and robustness, allowing for easy modifications or additions to the set of questions.

# Create a nested dictionary to store all the questions in an efficent way.
questions = [

# Add the questions that will be displayed for the Basic level - this is the easiest level of questions available.

{
    "difficulty":"BASIC",
    "question":" 5 + 3 = ___ ",
    "choices":["6","7","8","9"],
    "answer":"8"
},
{
    "difficulty":"BASIC",
    "question":" 2/4 equivalent to ___ ",
    "choices":["6/9","14/7","1/2","100/10"],
    "answer":"1/2"
},
{
    "difficulty":"BASIC",
    "question":"Area of a rectangle with l = 6 cm and w = 4 cm = ___",
    "choices":["10 cm²","20 cm²","24 cm²","30 cm²"],
    "answer":"24 cm²"
},
{
    "difficulty":"BASIC",
    "question":" 6 + 8 = ___ ",
    "choices":["12","13","14","15"],
    "answer":"14"
},
{
    "difficulty":"BASIC",
    "question":" 2x + x = ___ ",
    "choices":["2x²","2x","3x","x"],
    "answer":"3x"
},
{
    "difficulty":"BASIC",
    "question":" 14 - 9 = ___ ",
    "choices":["3","4","5","6"],
    "answer":"5"
},
{
    "difficulty":"BASIC",
    "question":" 8 × 5 = ___ ",
    "choices":["35","40","45","50"],
    "answer":"40"
},
{
    "difficulty":"BASIC",
    "question":" 27 ÷ 3 = ___ ",
    "choices":["7","8","9","10"],
    "answer":"9"
},
{
    "difficulty":"BASIC",
    "question":" 11 + 13 = ___ ",
    "choices":["22","23","24","25"],
    "answer":"24"
},
{
    "difficulty":"BASIC",
    "question":" 16 - 8 = ____ ",
    "choices":["6","7","8","9"],
    "answer":"8"
},
{
    "difficulty":"BASIC",
    "question":" 9 × 3 = ___ ",
    "choices":["18","27","36","24"],
    "answer":"27"
},
{
    "difficulty":"BASIC",
    "question":" 20 ÷ 4 = ___ ",
    "choices":["4","5","6","7"],
    "answer":"5"
},
{
    "difficulty":"BASIC",
    "question":" 30 + 15 = ___ ",
    "choices":["40","45","50","55"],
    "answer":"45"
},
{
    "difficulty":"BASIC",
    "question":" 19 - 7 = ___ ",
    "choices":["10","11","12","13"],
    "answer":"12"
},
{
    "difficulty":"BASIC",
    "question":" 2 × 11 = ___ ",
    "choices":["20","21","22","23"],
    "answer":"22"
},
{
    "difficulty":"BASIC",
    "question":" 42 ÷ 6 = ___ ",
    "choices":["6","7","8","9"],
    "answer":"7"
},
{
    "difficulty":"BASIC",
    "question":" 13 + 18 = ___ ",
    "choices":["30","31","32","33"],
    "answer":"31"
},
{
    "difficulty":"BASIC",
    "question":" 25 - 9 = ___ ",
    "choices":["15","16","17","18"],
    "answer":"16"
},
{
    "difficulty":"BASIC",
    "question":" 12 × 2 = ___ ",
    "choices":["22","23","24","26"],
    "answer":"24"
},
{
    "difficulty":"BASIC",
    "question":" 45 ÷ 5 = ___ ",
    "choices":["8","9","10","11"],
    "answer":"9"
},
{
    "difficulty":"BASIC",
    "question":" 1 x 5 = ___ ",
    "choices":["6","50","4","5"],
    "answer":"5"
},

{
    "difficulty":"BASIC",
    "question":" 9 - 4 = ___ ",
    "choices":["3","5","6","7"],
    "answer":"5"
},

{
    "difficulty":"BASIC",
    "question":" 7 × 6 = ___ ",
    "choices":["36","42","48","40"],
    "answer":"42"
},

{
    "difficulty":"BASIC",
    "question":" 18 ÷ 3 = ___ ",
    "choices":["5","6","7","8"],
    "answer":"6"
},

{
    "difficulty":"BASIC",
    "question":" 15 + 9 = ___ ",
    "choices":["24","25","26","23"],
    "answer":"24"
},{
    "difficulty":"BASIC",
    "question":" 4 + 7 = ___ ",
    "choices":["11","28","3","-3"],
    "answer":"11"
},{
    "difficulty":"BASIC",
    "question":" 3 x 6 = ___ ",
    "choices":["18","21","9","-18"],
    "answer":"18"
},
# Add questions for the Advanced difficulty level - slightly harder than the basic question set, and moderately challenging.

{
    "difficulty":"ADVANCED",
    "question":" 24 × 6 = ___ ",
    "choices":["124","144","134","154"],
    "answer":"144"
},
{
    "difficulty":"ADVANCED",
    "question":" 18 × 7 = ___ ",
    "choices":["116","126","136","146"],
    "answer":"126"
},
{
    "difficulty":"ADVANCED",
    "question":" 96 ÷ 8 = ___ ",
    "choices":["10","11","12","13"],
    "answer":"12"
},
{
    "difficulty":"ADVANCED",
    "question":" 25² = ___ ",
    "choices":["525","575","625","675"],
    "answer":"625"
},
{
    "difficulty":"ADVANCED",
    "question":" 2x × x = ___ ",
    "choices":["2x²","2x","3x","x"],
    "answer":"2x²"
},
{
    "difficulty":"ADVANCED",
    "question":" 13 × 12 = ___ ",
    "choices":["146","156","166","176"],
    "answer":"156"
},
{
    "difficulty":"ADVANCED",
    "question":" 144 ÷ 12 = ___ ",
    "choices":["10","11","12","13"],
    "answer":"12"
},
{
    "difficulty":"ADVANCED",
    "question":" 19² = ___ ",
    "choices":["341","351","361","371"],
    "answer":"361"
},
{
    "difficulty":"ADVANCED",
    "question":" 45 × 3 = ___ ",
    "choices":["125","130","135","140"],
    "answer":"135"
},
{
    "difficulty":"ADVANCED",
    "question":" 132 ÷ 11 = ___ ",
    "choices":["10","11","12","13"],
    "answer":"12"
},
{
    "difficulty":"ADVANCED",
    "question":" 28 × 5 = ___ ",
    "choices":["130","135","140","145"],
    "answer":"140"
},
{
    "difficulty":"ADVANCED",
    "question":" 22² = ___ ",
    "choices":["464","474","484","494"],
    "answer":"484"
},
{
    "difficulty":"ADVANCED",
    "question":" 15 × 18 = ___ ",
    "choices":["260","270","280","290"],
    "answer":"270"
},
{
    "difficulty":"ADVANCED",
    "question":" 169 ÷ 13 = ___ ",
    "choices":["11","12","13","14"],
    "answer":"13"
},
{
    "difficulty":"ADVANCED",
    "question":" 31 × 4 = ___ ",
    "choices":["120","122","124","126"],
    "answer":"124"
},
{
    "difficulty":"ADVANCED",
    "question":" 84 ÷ 7 = ___ ",
    "choices":["10","11","12","13"],
    "answer":"12"
},
{
    "difficulty":"ADVANCED",
    "question":" 29² = ___ ",
    "choices":["821","831","841","851"],
    "answer":"841"
},
{
    "difficulty":"ADVANCED",
    "question":" 56 × 2 = ___ ",
    "choices":["110","111","112","113"],
    "answer":"112"
},
{
    "difficulty":"ADVANCED",
    "question":"36 ÷ 4 = ___ ",
    "choices":["8","9","10","12"],
    "answer":"9"
},

{
    "difficulty":"ADVANCED",
    "question":"17² = ___ ",
    "choices":["279","289","299","309"],
    "answer":"289"
},

# Create the Expert questions - the final and most challenging difficulty level.
{
    "difficulty":"EXPERT",
    "question":"√144 = ___ ",
    "choices":["10","11","12","13"],
    "answer":"12"
},

{
    "difficulty":"EXPERT",
    "question":"5³ = ___ ",
    "choices":["25","75","100","125"],
    "answer":"125"
},
{
    "difficulty":"EXPERT",
    "question":"√225 = ___ ",
    "choices":["13","14","15","16"],
    "answer":"15"
},
{
    "difficulty":"EXPERT",
    "question":"7³ = ___ ",
    "choices":["243","343","443","543"],
    "answer":"343"
},
{
    "difficulty":"EXPERT",
    "question":"18² = ___ ",
    "choices":["314","324","334","344"],
    "answer":"324"
},
{
    "difficulty":"EXPERT",
    "question":"√196 = ___ ",
    "choices":["12","13","14","15"],
    "answer":"14"
},
{
    "difficulty":"EXPERT",
    "question":"9³ = ___ ",
    "choices":["629","729","829","929"],
    "answer":"729"
},
{
    "difficulty":"EXPERT",
    "question":"24² = ___ ",
    "choices":["556","566","576","586"],
    "answer":"576"
},
{
    "difficulty":"EXPERT",
    "question":"√324 = ___ ",
    "choices":["16","17","18","19"],
    "answer":"18"
},
{
    "difficulty":"EXPERT",
    "question":"11³ = ___ ",
    "choices":["1211","1311","1331","1431"],
    "answer":"1331"
},
{
    "difficulty":"EXPERT",
    "question":"26² = ___ ",
    "choices":["656","666","676","686"],
    "answer":"676"
},
{
    "difficulty":"EXPERT",
    "question":"√400 = ___ ",
    "choices":["18","19","20","21"],
    "answer":"20"
},
{
    "difficulty":"EXPERT",
    "question":"8³ = ___ ",
    "choices":["412","512","612","712"],
    "answer":"512"
},
{
    "difficulty":"EXPERT",
    "question":"35² = ___ ",
    "choices":["1125","1225","1325","1425"],
    "answer":"1225"
},
{
    "difficulty":"EXPERT",
    "question":"√289 = ___ ",
    "choices":["15","16","17","18"],
    "answer":"17"
},
{
    "difficulty":"EXPERT",
    "question":"12³ = ___ ",
    "choices":["1528","1628","1728","1828"],
    "answer":"1728"
},
{
    "difficulty":"EXPERT",
    "question":"32² = ___ ",
    "choices":["924","1024","1124","1224"],
    "answer":"1024"
},
{
    "difficulty":"EXPERT",
    "question":"√625 = ___ ",
    "choices":["23","24","25","26"],
    "answer":"25"
},
{
    "difficulty":"EXPERT",
    "question":"15² = ___ ",
    "choices":["215","225","235","245"],
    "answer":"225"
},

]
