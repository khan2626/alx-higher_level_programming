#!/usr/bin/node
exports.esrever = function (list) {
    let length = list.length - 1;
    let newlist = [];
    for (let i = length; i >= 0; i--) {
	newlist.push(list[i]);
    }
    return newlist;
};
