/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function(object) {
    if (object === null)
        return 'null';
    
    if (Array.isArray(object))
        return `[${object.map(e => jsonStringify(e)).join(',')}]`
    
    if (typeof object === 'object')
        return `{${Object.entries(object).map(([k, v], i) => `"${k}":${jsonStringify(v)}`).join(',')}}`
    
    if (typeof object === 'string')
        return `"${object}"`
    
    return String(object);
};