/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const _arr = [];
    arr.forEach((el, i) => _arr.push(fn(el, i)));
    return _arr;
};