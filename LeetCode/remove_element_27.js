let removeElement = (nums, value) => {
    let nums1 = nums.filter(number => number !== value )
    console.log(nums1)
    return nums1.length
}

console.log(removeElement([3,2,2,3], 3))