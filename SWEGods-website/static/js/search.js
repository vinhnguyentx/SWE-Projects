
console.log("GOD AND");
console.log(godand.name);
console.log("HERO AND");
console.log(heroand.name);
console.log("LOCATION AND");
console.log(locationand.name);
console.log("MYTH AND");
console.log(mythand.name);
console.log("GOD AND");
console.log(godor.name);
console.log("HERO AND");
console.log(heroor.name);
console.log("LOCATION AND");
console.log(locationor.name);
console.log("MYTH AND");
console.log(mythor.name);

var godandrep = godand.name;
if( typeof godandrep == 'string') {
    godandrep = godandrep.replace(/'{/g, "{");
    godandrep = godandrep.replace(/}'/g, "}");
    console.log('REPLACE');
    console.log(godandrep);
}

var godandobject = {};

try {
    godandobject = JSON.parse(godandrep);
    }
catch (e)
{
    console.log(e);
}

var heroandrep = heroand.name;
if(typeof heroandrep == 'string') {
    heroandrep = heroandrep.replace(/'{/g, "{");
    heroandrep = heroandrep.replace(/}'/g, "}");
    console.log('REPLACE');
    console.log(heroandrep);
}
var heroandobject = {};

try {
    heroandobject = JSON.parse(heroandrep);
    }
catch (e)
{
    console.log(e);
}

var locationandrep = locationand.name;
if(typeof locationandrep == 'string') {
    locationandrep = locationandrep.replace(/'{/g, "{");
    locationandrep = locationandrep.replace(/}'/g, "}");
    console.log('REPLACE');
    console.log(locationandrep);
}
var locationandobject = {};

try {
    locationandobject = JSON.parse(locationandrep);
    }
catch (e)
{
    console.log(e);
}

var mythandrep = mythand.name;
if(typeof mythandrep == 'string') {
    mythandrep = mythandrep.replace(/'{/g, "{");
    mythandrep = mythandrep.replace(/}'/g, "}");
    console.log('REPLACE');
    console.log(mythandrep);
}
var mythandobject = {};

try {
    mythandobject = JSON.parse(mythandrep);
    }
catch (e)
{
    console.log(e);
}


// var mythandrep = mythand.name.replace(/'{/g, "{");
// mythandrep = mythandrep.replace(/}'/g, "}");
// console.log('REPLACE');
// console.log(mythandrep);
// var mythandobject = JSON.parse(mythandrep);

var godorrep = godor.name;
if( typeof godorrep == 'string') {
    godorrep = godorrep.replace(/'{/g, "{");
    godorrep = godorrep.replace(/}'/g, "}");
    console.log('REPLACE');
    console.log(godorrep);
}

var godorobject = {};

try {
    godorobject = JSON.parse(godorrep);
    }
catch (e)
{
    console.log(e);
}

var heroorrep = heroor.name;
if(typeof heroorrep == 'string') {
    heroorrep = heroorrep.replace(/'{/g, "{");
    heroorrep = heroorrep.replace(/}'/g, "}");
    console.log('REPLACE');
    console.log(heroorrep);
}
var heroorobject = {};

try {
    heroorobject = JSON.parse(heroorrep);
    }
catch (e)
{
    console.log(e);
}

var locationorrep = locationor.name;
if(typeof locationorrep == 'string') {
    locationorrep = locationorrep.replace(/'{/g, "{");
    locationorrep = locationorrep.replace(/}'/g, "}");
    console.log('REPLACE');
    console.log(locationorrep);
}
var locationorobject = {};

try {
    locationorobject = JSON.parse(locationorrep);
    }
catch (e)
{
    console.log(e);
}


var mythorrep = mythor.name;
if(typeof mythorrep == 'string') {
    mythorrep = mythorrep.replace(/'{/g, "{");
    mythorrep = mythorrep.replace(/}'/g, "}");
    console.log('REPLACE');
    console.log(mythorrep);
}
var mythorobject = {};

try {
    mythorobject = JSON.parse(mythorrep);
    }
catch (e)
{
    console.log(e);
}

// var mythorrep = mythor.name.replace(/'{/g, "{");
// mythorrep = mythorrep.replace(/}'/g, "}");
// console.log('REPLACE');
// console.log(mythorrep);
// var mythorobject = JSON.parse(mythorrep);

console.log('GOD AND OBJ');
console.log(godandobject);
console.log('HERO AND OBJ');
console.log(heroandobject);
console.log('LOCATION AND OBJ');
console.log(locationandobject);
console.log('MYTH AND OBJ');
console.log(mythandobject);
console.log('GOD OR OBJ');
console.log(godorobject);
console.log('HERO OR OBJ');
console.log(heroorobject);
console.log('LOCATION OR OBJ');
console.log(locationorobject);
console.log('MYTH OR OBJ');
console.log(mythorobject);



var Table = Reactable.Table,
    unsafe = Reactable.unsafe;

var bgColors = { "Default": "#81b71a",
                    "Blue": "#00B1E1",
                    "Cyan": "#37BC9B",
                    "Green": "#8CC152",
                    "Red": "#E9573F",
                    "Yellow": "#F6BB42",
};

var godsinfoand = [];
for (var i = 0; i < godandobject.length; i++) {
    var hrefname = godandobject[i].name.replace('<b>', '');
    var hrefname = hrefname.replace('</b>', '');
    var god = {
      'Name': unsafe('<a href="/gods/' + hrefname.toLowerCase() + '">' + godandobject[i].name + '</a>'),
      'Roman Name': unsafe(godandobject[i].romanname),
      'Symbol': unsafe(godandobject[i].symbol),
      'Power': unsafe(godandobject[i].power),
      'Father': unsafe(godandobject[i].father),
      'Mother': unsafe(godandobject[i].mother)
    };
      godsinfoand.push(god);
}

var heroesinfoand = [];
for (var i = 0; i < heroandobject.length; i++) {
    var hrefname = heroandobject[i].name.replace('<b>', '');
    var hrefname = hrefname.replace('</b>', '');
    var hero = {
      'Name': unsafe('<a href="/heroes/' + hrefname.toLowerCase() + '">' + heroandobject[i].name + '</a>'),
      'Type': unsafe(heroandobject[i].herotype),
      'Power': unsafe(heroandobject[i].power),
      'Home': unsafe(heroandobject[i].home),
      'Father': unsafe(heroandobject[i].father),
      'Mother': unsafe(heroandobject[i].mother)
    };
    heroesinfoand.push(hero);
}

var locationsinfoand = [];
for (var i = 0; i < locationandobject.length; i++) {
    var hrefname = locationandobject[i].name.replace('<b>', '');
    var hrefname = hrefname.replace('</b>', '');
    var location = {
      'Name': unsafe('<a href="/locations/' + hrefname.toLowerCase() + '">' + locationandobject[i].name + '</a>'),
      'Alternate Name': unsafe(locationandobject[i].altname),
      'Type': unsafe(locationandobject[i].locationtype),
      'Myth': unsafe(locationandobject[i].myth),
      'Characters': unsafe(locationandobject[i].gods)
    };
    locationsinfoand.push(location);
}

var mythsinfoand = [];
for (var i = 0; i < mythandobject.length; i++) {
    var myth = {
      'Name': unsafe('<a href="/myths/' + mythandobject[i].name.toLowerCase() + '">' + mythandobject[i].name + '</a>'),
      'Description': unsafe(mythandobject[i].description),
      'Theme': unsafe(mythandobject[i].theme),
      'Place': unsafe(mythandobject[i].place),
      'Gods': unsafe(mythandobject[i].gods),
      'Non-Gods': unsafe(mythandobject[i].nongods)
    };
    mythsinfoand.push(myth);
}

var godsinfoor = [];
for (var i = 0; i < godorobject.length; i++) {
    var hrefname = godorobject[i].name.replace('<b>', '');
    var hrefname = hrefname.replace('</b>', '');
    var god = {
      'Name': unsafe('<a href="/gods/' + hrefname.toLowerCase() + '">' + godorobject[i].name + '</a>'),
      'Roman Name': unsafe(godorobject[i].romanname),
      'Symbol': unsafe(godorobject[i].symbol),
      'Power': unsafe(godorobject[i].power),
      'Father': unsafe(godorobject[i].father),
      'Mother': unsafe(godorobject[i].mother)
    };
    godsinfoor.push(god);
}

var heroesinfoor = [];
for (var i = 0; i < heroorobject.length; i++) {
    var hrefname = heroorobject[i].name.replace('<b>', '');
    var hrefname = hrefname.replace('</b>', '');
    var hero = {
      'Name': unsafe('<a href="/heroes/' + hrefname.toLowerCase() + '">' + heroorobject[i].name + '</a>'),
      'Type': unsafe(heroorobject[i].herotype),
      'Power': unsafe(heroorobject[i].power),
      'Home': unsafe(heroorobject[i].home),
      'Father': unsafe(heroorobject[i].father),
      'Mother': unsafe(heroorobject[i].mother)
    };
    heroesinfoor.push(hero);
}

var locationsinfoor = [];
for (var i = 0; i < locationorobject.length; i++) {
    var hrefname = locationorobject[i].name.replace('<b>', '');
    var hrefname = hrefname.replace('</b>', '');
    var location = {
      'Name': unsafe('<a href="/locations/' + hrefname.toLowerCase() + '">' + locationorobject[i].name + '</a>'),
      'Alternate Name': unsafe(locationorobject[i].altname),
      'Type': unsafe(locationorobject[i].locationtype),
      'Myth': unsafe(locationorobject[i].myth),
      'Characters': unsafe(locationorobject[i].gods)
    };
    locationsinfoor.push(location);
}

var mythsinfoor = [];
for (var i = 0; i < mythorobject.length; i++) {
    var myth = {
      'Name': unsafe('<a href="/myths/' + mythorobject[i].name.toLowerCase() + '">' + mythorobject[i].name + '</a>'),
      'Description': unsafe(mythorobject[i].description),
      'Theme': unsafe(mythorobject[i].theme),
      'Place': unsafe(mythorobject[i].place),
      'Gods': unsafe(mythorobject[i].gods),
      'Non-Gods': unsafe(mythorobject[i].nongods)
    };
    mythsinfoor.push(myth);
}

ReactDOM.render(
  <div>
    <h3>AND RESULTS</h3>
    <h4>Gods</h4>
    <div>
      <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

      data={godsinfoand}

      sortable={[
        {
            column: 'Name',
            sortFunction: function(a, b){
                // Sort by last name
                var nameA = a
                var nameB = b

                return nameA.localeCompare(nameB);
            }
        },
        'Roman Name',
        'Symbol',
        'Power',
        'Father',
        'Mother'
      ]}

      filterable={['Name', 'Roman Name', 'Symbol', 'Power', 'Father', 'Mother']}

      defaultSort={{column: 'Name', direction: 'asc'}} itemsPerPage={8} pageButtonLimit={100}/>
    </div>
    <h4>Heroes</h4>
    <div>
      <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

      data={heroesinfoand}

      sortable={[
        {
            column: 'Name',
            sortFunction: function(a, b){
                // Sort by last name
                var nameA = a
                var nameB = b

                return nameA.localeCompare(nameB);
            }
        },
        'Type',
        'Power',
        'Home',
        'Father',
        'Mother'
      ]}

      filterable={['Name', 'Type', 'Power', 'Home', 'Father', 'Mother']}

      defaultSort={{column: 'Name', direction: 'asc'}} itemsPerPage={8} pageButtonLimit={100}/>
    </div>
    <h4>Locations</h4>
    <div>
      <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

      data={locationsinfoand}

      sortable={[
        {
            column: 'Name',
            sortFunction: function(a, b){
                // Sort by last name
                var nameA = a
                var nameB = b

                return nameA.localeCompare(nameB);
            }
        },
        'Alternate Name',
        'Type',
        'Myth',
        'Characters'
      ]}

      filterable={['Name', 'Alternate Name', 'Type', 'Myth', 'Characters']}

      defaultSort={{column: 'Name', direction: 'asc'}} itemsPerPage={8} pageButtonLimit={100}/>
    </div>
    <h4>Myths</h4>
    <div>
      <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

      data={mythsinfoand}

      sortable={[
        {
            column: 'Name',
            sortFunction: function(a, b){
                // Sort by last name
                var nameA = a
                var nameB = b

                return nameA.localeCompare(nameB);
            }
        },
        'Description',
        'Theme',
        'Place',
        'Gods',
        'Characters'
      ]}

      filterable={['Name', 'Description', 'Theme', 'Place', 'Gods', 'Characters']}

      defaultSort={{column: 'Name', direction: 'asc'}} itemsPerPage={3} pageButtonLimit={100}/>
    </div>
    <h3>OR RESULTS</h3>
    <h4>Gods</h4>
    <div>
      <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

      data={godsinfoor}

      sortable={[
        {
            column: 'Name',
            sortFunction: function(a, b){
                // Sort by last name
                var nameA = a
                var nameB = b

                return nameA.localeCompare(nameB);
            }
        },
        'Roman Name',
        'Symbol',
        'Power',
        'Father',
        'Mother'
      ]}

      filterable={['Name', 'Roman Name', 'Symbol', 'Power', 'Father', 'Mother']}

      defaultSort={{column: 'Name', direction: 'asc'}} itemsPerPage={8} pageButtonLimit={100}/>
    </div>
    <h4>Heroes</h4>
    <div>
      <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

      data={heroesinfoor}

      sortable={[
        {
            column: 'Name',
            sortFunction: function(a, b){
                // Sort by last name
                var nameA = a
                var nameB = b

                return nameA.localeCompare(nameB);
            }
        },
        'Type',
        'Power',
        'Home',
        'Father',
        'Mother'
      ]}

      filterable={['Name', 'Type', 'Power', 'Home', 'Father', 'Mother']}

      defaultSort={{column: 'Name', direction: 'asc'}} itemsPerPage={8} pageButtonLimit={100}/>
    </div>
    <h4>Locations</h4>
    <div>
      <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

      data={locationsinfoor}

      sortable={[
        {
            column: 'Name',
            sortFunction: function(a, b){
                // Sort by last name
                var nameA = a
                var nameB = b

                return nameA.localeCompare(nameB);
            }
        },
        'Alternate Name',
        'Type',
        'Myth',
        'Characters'
      ]}

      filterable={['Name', 'Alternate Name', 'Type', 'Myth', 'Characters']}

      defaultSort={{column: 'Name', direction: 'asc'}} itemsPerPage={8} pageButtonLimit={100}/>
    </div>
    <h4>Myths</h4>
    <div>
      <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

      data={mythsinfoor}

      sortable={[
        {
            column: 'Name',
            sortFunction: function(a, b){
                // Sort by last name
                var nameA = a
                var nameB = b

                return nameA.localeCompare(nameB);
            }
        },
        'Description',
        'Theme',
        'Place',
        'Gods',
        'Characters'
      ]}

      filterable={['Name', 'Description', 'Theme', 'Place', 'Gods', 'Characters']}

      defaultSort={{column: 'Name', direction: 'asc'}} itemsPerPage={3} pageButtonLimit={100}/>
    </div>
  </div>,
    document.getElementById('search')
);
