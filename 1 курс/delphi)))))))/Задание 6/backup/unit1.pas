unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Grids, Menus,
  ExtCtrls;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Button2: TButton;
    Button3: TButton;
    Edit1: TEdit;
    Edit2: TEdit;
    Image1: TImage;
    Label1: TLabel;
    Label2: TLabel;
    Label3: TLabel;
    Label4: TLabel;
    StringGrid1: TStringGrid;
    procedure Button1Click(Sender: TObject);
    procedure Button2Click(Sender: TObject);
    procedure Button3Click(Sender: TObject);
    procedure FormShow(Sender: TObject);

  private

  public

  end;

var
  Form1: TForm1;
  i: integer;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
type
TPerson = record
Name: String;
Num: integer;
end;
var
  mas: array[0..4] of Tperson;
begin
  if i<=4 then begin
  with mas[i] do begin

      Name:=edit1.text;
      Num:=strtoint(edit2.text);
      edit1.text:='';
      edit2.text:='';
      stringgrid1.cells[0,i]:=mas[i].name;
      stringgrid1.cells[1,i]:=inttostr(mas[i].num);
    end;
   i:=i+1;
  end
  else showmessage('таблица заполнена');

end;

procedure TForm1.Button2Click(Sender: TObject);
var
  i,j: integer;
  d1, d2, d3, d4: string;

begin
  for i:=0 to 4 do
    for j:=i+1 to 4 do begin
        if (stringgrid1.cells[1,i])<(stringgrid1.cells[1,j]) then begin
        d1:=stringgrid1.cells[1,i];
        d2:=stringgrid1.cells[1,j];
        d3:=stringgrid1.cells[0,i];
        d4:=stringgrid1.cells[0,j];
        stringgrid1.cells[1,i]:=d2;
        stringgrid1.cells[1,j]:=d1;
        stringgrid1.cells[0,i]:=d4;
        stringgrid1.cells[0,j]:=d3;
        end;



end;
end;

procedure TForm1.Button3Click(Sender: TObject);
var
  k: integer;
begin
  for k:=0 to 4 do begin
      stringgrid1.cells[0,k]:='';
      stringgrid1.cells[1,k]:='';

  end;
  i:=0;
end;

procedure TForm1.FormShow(Sender: TObject);
begin
  i:=0;
end;


end.

