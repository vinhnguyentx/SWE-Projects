console.log(LocationsList);

var godbunch = [];
var herobunch = [];
var mythbunch = [];

for (var i = 0; i < GodsList.length; i++) {
  godbunch.push(GodsList[i].name.toLowerCase());
}

for (var i = 0; i < HeroesList.length; i++) {
  herobunch.push(HeroesList[i].name.toLowerCase());
}

for (var i = 0; i < MythsList.length; i++) {
  herobunch.push(MythsList[i].name.toLowerCase());
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

var locationsinfo = [];
for (var i = 0; i < LocationsList.length; i++) {
    var mythname = LocationsList[i].myth;

    if (mythbunch.indexOf(LocationsList[i].myth.toLowerCase()) !== -1) {
      mythname = '<a href="/gods/' + LocationsList[i].myth.toLowerCase() + '">' + LocationsList[i].myth+ '</a>';
    }

    var location = {
      'Name': unsafe('<a href="/locations/' + LocationsList[i].name.toLowerCase() + '">' + LocationsList[i].name + '</a>'),
      'Alternate Name': unsafe(LocationsList[i].altname),
      'Type': unsafe(LocationsList[i].locationtype),
      'Myth': unsafe(mythname),
      'Characters': unsafe(LocationsList[i].gods)
    };
    locationsinfo.push(location);
}

ReactDOM.render(
  <div>
    <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

    data={locationsinfo}

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
  </div>,
    document.getElementById('locations')
);
