/**
 * @param {object} obj1
 * @param {object} obj2
 * @return {object}
 */
function objDiff(obj1, obj2) {
    if (obj1 === obj2)
        return {};
    else if (obj1 === null || obj2 === null)
        return [obj1, obj2];
    else if (typeof obj1 !== "object" || typeof obj2 !== "object")
        return [obj1, obj2];
    else if (Array.isArray(obj1) !== Array.isArray(obj2))
        return [obj1, obj2];
    
    const result = {};
    
    Object.entries(obj1).forEach(([k, v]) => {
        if (k in obj2) {
            const subDiff = objDiff(v, obj2[k]);
            if (Object.keys(subDiff).length > 0)
                result[k] = subDiff;
        }
    });
    
    return result;
};