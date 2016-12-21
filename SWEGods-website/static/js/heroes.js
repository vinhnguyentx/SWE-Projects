console.log(HeroesList);

var godbunch = [];
var herobunch = [];
var locationbunch = [];

for (var i = 0; i < GodsList.length; i++) {
  godbunch.push(GodsList[i].name.toLowerCase());
}

for (var i = 0; i < HeroesList.length; i++) {
  herobunch.push(HeroesList[i].name.toLowerCase());
}

for (var i = 0; i < LocationsList.length; i++) {
  locationbunch.push(LocationsList[i].name.toLowerCase());
}

var Table = Reactable.Table,
    unsafe = Reactable.unsafe;

var bgColors = { "Default": "#81b71a",
                    "Blue": "#00B1E1",
                    "Cyan": "#37BC9B",
                    "Green": "#8CC152",
                    "Red": "#E9573F",
                    "Yellow": "#F6BB42",
};

var heroesinfo = [];
for (var i = 0; i < HeroesList.length; i++) {
    var fathername = HeroesList[i].father;
    var mothername = HeroesList[i].mother;
    var locationname = HeroesList[i].home;

    if (godbunch.indexOf(HeroesList[i].father.toLowerCase()) !== -1) {
      fathername = '<a href="/gods/' + HeroesList[i].father.toLowerCase() + '">' + HeroesList[i].father+ '</a>';
    }
    if (herobunch.indexOf(HeroesList[i].father.toLowerCase()) !== -1) {
      fathername = '<a href="/heroes/' + HeroesList[i].father.toLowerCase() + '">' + HeroesList[i].father + '</a>';
    }
    if (godbunch.indexOf(HeroesList[i].mother.toLowerCase()) !== -1) {
      mothername = '<a href="/gods/' + HeroesList[i].mother.toLowerCase() + '">' + HeroesList[i].mother + '</a>';
    }
    if (herobunch.indexOf(HeroesList[i].mother.toLowerCase()) !== -1) {
      mothername = '<a href="/heroes/' + HeroesList[i].mother.toLowerCase() + '">' + HeroesList[i].mother + '</a>';
    }
    if (locationbunch.indexOf(HeroesList[i].home.toLowerCase()) !== -1) {
      locationname = '<a href="/locations/' + HeroesList[i].home.toLowerCase() + '">' + HeroesList[i].home + '</a>';
    }

    var hero = {
      'Name': unsafe('<a href="/heroes/' + HeroesList[i].name.toLowerCase() + '">' + HeroesList[i].name + '</a>'),
      'Type': unsafe(HeroesList[i].herotype),
      'Power': unsafe(HeroesList[i].power),
      'Home': unsafe(locationname),
      'Father': unsafe(fathername),
      'Mother': unsafe(mothername)
    };
    heroesinfo.push(hero);
}

ReactDOM.render(
  <div>
    <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

    data={heroesinfo}

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
  </div>,
    document.getElementById('heroes')
);
