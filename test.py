
txt = """
<td align="left" bgcolor="white" colspan="2" valign="top"> <div align="left">
<p class="style2"><span class="style1 style1">  Food-Info.net&gt; E-numbers &gt;<a href="e100-200.htm"> E100-200</a> </span></p>
<h1 align="center"><strong>E100: Curcumin </strong></h1>
<p><strong>E100 (i): Curcumin </strong><br/>
<strong>E100 (ii): Turmeric </strong><br/>
<strong>CI 75300, Natural Yellow 3, diferuloylmethane </strong> </p>

<p><strong>Origin: <br/>
</strong>Natural colour isolated from the roots and stem of Yellowroot (<em>Curcuma longa </em> and <em>Curcuma domestica</em>). Turmeric is the crude extract, whereas curcumin is the purified compound. It imparts the yellow colour to curry powder. More on curcumin, click <a href="../colour/curcumin.htm"><strong>here</strong></a>. </p>

<p><strong>Function &amp; characteristics: <br/>
</strong>Food colour, whose colour ranges from yellow to red, depending on pH (acidity). It is not very soluble in water. </p>

<p><strong>Products: <br/>
</strong>Many different products. </p>

<p><strong>Daily intake: <br/>
</strong>Up to 1 mg/kg body weight for curcumin, and 0.3 mg/kg for turmeric. </p>

<p><strong>Side effects: <br/>
</strong>No side effects known in the concentrations used in foods. </p>

<p><strong>Dietary restrictions: <br/>
</strong>None; E100 can be consumed by all religious groups, vegans and vegetarians. <strong>
</strong>
</p>

<h1 align="center"> </h1>
</div></td>
"""

a = txt

title = a.split('<h1 align="center"><strong>')[1].split('</strong></h1>\n<p><strong>')[0].strip()
origin = a.split('<p><strong>Origin: <br/>')[1].split("</p>")[0]
function = a.split('<p><strong>Function &amp; characteristics: <br/>')[1].split("</p>")[0]
products = a.split('<p><strong>Products: <br/>')[1].split("</p>")[0]
daily_intake = a.split('<p><strong>Daily intake: <br/>')[1].split("</p>")[0]
side_effects = a.split('<p><strong>Side effects: <br/>')[1].split("</p>")[0]
function = a.split('<p><strong>Dietary restrictions: <br/>')[1].split("</p>")[0]


def sanitize(a: str):
    a = a.strip()
    if '</a>' in a:
        a = a.replace(a.split('<a')[1].split('</a>')[0], "").replace("<a</a>", "")
    kw = ("<strong>", "</strong>", "<em>", "</em>", "\n", "\t", "<i>", "</i>")
    for i in kw:
        a = a.replace(i, "")
    return a


print(sanitize(origin))
