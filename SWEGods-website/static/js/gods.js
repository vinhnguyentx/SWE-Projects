console.log(GodsList);

var godbunch = [];
var herobunch = [];
for (var i = 0; i < GodsList.length; i++) {
  godbunch.push(GodsList[i].name.toLowerCase());
}

for (var i = 0; i < HeroesList.length; i++) {
  herobunch.push(HeroesList[i].name.toLowerCase());
}
console.log(godbunch);
console.log(herobunch);


var Table = Reactable.Table,
    unsafe = Reactable.unsafe;

var bgColors = { "Default": "#81b71a",
                    "Blue": "#00B1E1",
                    "Cyan": "#37BC9B",
                    "Green": "#8CC152",
                    "Red": "#E9573F",
                    "Yellow": "#F6BB42",
};

var godsinfo = [];
for (var i = 0; i < GodsList.length; i++) {
    var fathername = GodsList[i].father;
    var mothername = GodsList[i].mother;

    if (godbunch.indexOf(GodsList[i].father.toLowerCase()) !== -1) {
      fathername = '<a href="/gods/' + GodsList[i].father.toLowerCase() + '">' + GodsList[i].father+ '</a>';
    }
    if (herobunch.indexOf(GodsList[i].father.toLowerCase()) !== -1) {
      fathername = '<a href="/heroes/' + GodsList[i].father.toLowerCase() + '">' + GodsList[i].father + '</a>';
    }
    if (godbunch.indexOf(GodsList[i].mother.toLowerCase()) !== -1) {
      mothername = '<a href="/gods/' + GodsList[i].mother.toLowerCase() + '">' + GodsList[i].mother + '</a>';
    }
    if (herobunch.indexOf(GodsList[i].mother.toLowerCase()) !== -1) {
      mothername = '<a href="/heroes/' + GodsList[i].mother.toLowerCase() + '">' + GodsList[i].mother + '</a>';
    }

    var god = {
      'Name': unsafe('<a href="/gods/' + GodsList[i].name.toLowerCase() + '">' + GodsList[i].name + '</a>'),
      'Roman Name': unsafe(GodsList[i].romanname),
      'Symbol': unsafe(GodsList[i].symbol),
      'Power': unsafe(GodsList[i].power),
      'Father': unsafe(fathername),
      'Mother': unsafe(mothername)
    };
    godsinfo.push(god);
}

ReactDOM.render(
  <div>
    <Table className="table" id="table" style={{backgroundColor: bgColors.Yellow}}

    data={godsinfo}

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
  </div>,
    document.getElementById('gods')
);
