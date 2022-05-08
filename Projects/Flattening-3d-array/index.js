const flatten = (array) => {
    // check if array is 3D
    if (array.length !== 3) {
        console.error("It Have to be 3D array");
        return;
    }
    // check if inner array is of equal length
    else if (array[0].length !== array[1].length || array[1].length !== array[2].length) {
        console.error("It Have to be 3D array with equal sized");
        return;
    }
    else {
        console.log([...array[0], ...array[1], ...array[2]]);

    }


}

// Example :
flatten([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);