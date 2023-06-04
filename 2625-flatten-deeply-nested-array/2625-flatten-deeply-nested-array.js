/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    let res = [];
    
    function flattening(_arr, depth) {
        _arr.forEach(el => {
            if (Array.isArray(el) && depth > 0)
                flattening(el, depth - 1);
            else
                res.push(el);
        });
    }
    
    flattening(arr, n);
    return res;
};