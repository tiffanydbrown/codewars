// DESCRIPTION:
// There was a test in your class and you passed it. Congratulations!
// But you're an ambitious person. You want to know if you're better than the average student in your class.

// You receive an array with your peers' test scores. Now calculate the average and compare your score!

// Return True if you're better, else False!

//My Solution:
function betterThanAverage(classPoints, yourPoints) {
    // Your code here
    //avg = scores + scores / # of scores added
    let sum = 0;
    for (let i = 0; i < classPoints.length; i++) {
      sum += classPoints[i];
    }
    let classAverage = sum / classPoints.length;
    
    return yourPoints >= classAverage;
  }