/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    const res = {};
    
    this.forEach(el => {
        const key = fn(el);
        
        if (key in res)
            res[key].push(el);
        else
            res[key] = [el];
    });
    
    return res;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */