const subSignBasicLookupTable = new Map(
[
	["A", [1, 60]],
	["B", [1, 12]],
	["C", [1, 20]],
	["D", [1, 70]],
	["E", [1, 40]],
	["F", [1, 60]],
	["G", [1, 54]],
	["H", [1, 8]],
	["I", [1, 15]],
	["K", [1, 24]],
	["L", [1, 7]],
	["M", [1, 44]],
	["N", [1, 42]],
	["O", [1, 51]],
	["P", [1, 11]],
	["Q", [1, 7]],
	["R", [1, 25]],
	["S", [1, 45]],
	["T", [1, 35]],
	["U", [1, 41]],
	["V", [1, 40]],
	["X", [1, 25]],
	["Y", [1, 8]],
	["Z", [1, 8]],
	["AA", [1, 41]]
]);

const subSignVariantLookupTable = new Map(
[
	["Y1", [1, 1]],	// A-A
]);

function getGardinerSubSignList(prefix)
{
	let list = [];
	if(subSignBasicLookupTable.has(prefix) == false)
	{
		return list;
	}
	
	const basicLookup = subSignBasicLookupTable.get(prefix);
	for(let i = basicLookup[0]; i <= basicLookup[1]; ++i)
	{
		const baseSign = prefix + i;
		list.push(baseSign);
		if(subSignVariantLookupTable.has(baseSign))
		{
			const subLookup = subSignVariantLookupTable.get(baseSign);
			for(let j = subLookup[0]; j <= subLookup[1]; ++j)
			{
				list.push(baseSign + String.fromCharCode(64 + j));
			}
		}
	}
	
	return list;
}
