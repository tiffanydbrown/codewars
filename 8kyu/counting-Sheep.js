function countSheeps(sheep) {
    let count = 0;
  
    for (let i = 0; i < sheep.length; i++) {
      if(sheep[i]) {
        count++;
      }
    }
      return count;
  }