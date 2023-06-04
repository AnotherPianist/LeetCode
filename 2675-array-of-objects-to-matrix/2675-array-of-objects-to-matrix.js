/**
 * @param {Array} arr
 * @return {Matrix}
 */
var jsonToMatrix = function(arr) {
    const isObject = x => (x !== null && typeof x === "object");
    
    function getKeys(obj) {
        if (!isObject(obj))
            return [""];
        
        const result = [];
        
        Object.keys(obj).forEach(k => {
            const childKeys = getKeys(obj[k]);
            childKeys.forEach(childK => result.push(childK ? `${k}.${childK}` : k));
        });
        
        return result;
    }
    
    const keysSet = arr.reduce((acc, curr) => {
        getKeys(curr).forEach(k => acc.add(k));
        
        return acc;
    }, new Set());
    
    const keys = Array.from(keysSet).sort();
    
    function getValue(obj, path) {
        const paths = path.split('.');
        
        let i = 0;
        let val = obj;
        
        while (i < paths.length) {
            if (!isObject(val))
                break;
            val = val[paths[i++]];
        }
        
        if (i < paths.length || isObject(val) || val === undefined)
            return "";
        return val;
    }
    
    const matrix = [keys];
    
    arr.forEach(obj => matrix.push(keys.map(key => getValue(obj, key))));
    
    return matrix;
};