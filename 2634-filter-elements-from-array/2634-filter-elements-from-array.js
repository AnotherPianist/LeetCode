/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const _arr = [];
    arr.forEach((el, i) => fn(el, i) && _arr.push(el));
    return _arr;
};