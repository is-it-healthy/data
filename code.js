data = {
    "100": {
        "code": "E100(ii)",
        "name": "Turmeric",
        "href": "e100.htm",
        "function": "Orange-yellow colour",
        "more_info": {
            "origin": "Natural colour isolated from the roots and stem of Yellowroot (Curcuma longa  and Curcuma domestica). Turmeric is the crude extract, whereas curcumin is the purified compound. It imparts the yellow colour to curry powder. More on curcumin, click .",
            "characteristics": "Food colour, whose colour ranges from yellow to red, depending on pH (acidity). It is not very soluble in water.",
            "products": "Many different products.",
            "dailt_intake": "Up to 1 mg/kg body weight for curcumin, and 0.3 mg/kg for turmeric.",
            "side_effects": "No side effects known in the concentrations used in foods.",
            "dietary_restrictions": "None; E100 can be consumed by all religious groups, vegans and vegetarians. "
        }
    },
    "101": {
        "code": "E101(ii)",
        "name": "Riboflavin- 5'- Phosphate",
        "href": "e101.htm",
        "function": "Yellow colour, vitamin B2",
        "more_info": {
            "origin": "Natural colour present in many foods such as milk, eggs, liver and vegetables. Commercially prepared from yeasts. It is also manufactured synthetically.",
            "characteristics": "Yellow food colour. Not very soluble in water.",
            "products": "Many different products.",
            "dailt_intake": "Up to 0.5 mg/kg body weight.",
            "side_effects": "No side effects known in the concentrations used in foods.",
            "dietary_restrictions": "None; E101 can be consumed by all religious groups, vegans and vegetarians. Although it can be produced from milk, this is not done commercially."
        }
    },
    "102": {
        "code": "E102",
        "name": "Tartrazine",
        "href": "e102.htm",
        "function": "Yellow colour, azo dye",
        "more_info": {
            "origin": "Synthetic azo dye. See  for a background on azo dyes.",
            "characteristics": "Yellow food colour. Very soluble in water.",
            "products": "Many different products.",
            "dailt_intake": "Up to 7.5 mg/kg body weight.",
            "side_effects": "Tartrazine is an azo dye. No side effects are known for pure tartrazine, except in people who are intolerant to salicylates (aspirin, berries, fruits); in that case tartrazine also induces intolerance symptoms. In combination with benzoates (E210-215), tartrazine is implicated in a large percentage of cases of ADHD syndrome (hyperactivity) in children. Asthmatics may also experience symptoms following consumption of tartrazine, as it is a known histamine-liberating agent.",
            "dietary_restrictions": "None; E102 can be consumed by all religious groups, vegans and vegetarians."
        }
    }
}

function splitToList(txt) {
    var items = [];
    var lis = txt.split(',');
    for (var i = 0; i < lis.length; i++) {
        items.push(lis[i].trim());
    }
    return items;
}

function getECodeData(eCodes_list) {
    var eCodes_data = [];
    for (var key in data) {
        if (eCodes_list.includes(key)) {
            eCodes_data.push(data[key]);
        }
    }
    return eCodes_data
}

function displaySideEffects(eCodes_data) {
    $("#mainSideEffectsList").empty();

    if (eCodes_data.length === 0) {
        // if eCodes_data is empty
        $("#mainSideEffectsList").append("<li class='list-item'>Please search to display results</li>");
    } else {
        // iterate through each item in eCodes_data and add it as a li
        for (var i = 0; i < eCodes_data.length; i++) {
            var listItem = $("<li class='list-item'></li>").text(eCodes_data[i].name);
            $("#mainSideEffectsList").append(listItem);
        }
    }
}

function displayAdditionalInformation(eCodes_data) {
    $('#additionalEffectsList').empty();

    for (var i = 0; i < eCodes_data.length; i++) {
        var li = $('<li>');
        var h3 = $('<h3>').text(eCodes_data[i].name);
        var p = $('<p>').text(eCodes_data[i].function);

        li.append(h3);
        li.append(p);

        $('#additionalEffectsList').append(li);
    }
}

$(document).ready(function () {

    $('#searchButton').click(function () {

        var inputText = $("#searchInput").val();
        var eCodes_list = splitToList(inputText);
        var eCodes_data = getECodeData(eCodes_list);
        displaySideEffects(eCodes_data);
        displayAdditionalInformation(eCodes_data);

        console.log(eCodes_data);

    });

});