unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, Forms, Controls, Graphics, Dialogs, StdCtrls, Grids;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    ListBox1: TListBox;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;
  f: textfile;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
var
  s: string;
  len: integer;
  i: integer;
  s2: string;

begin
  AssignFile(f, 'file.txt');
  if FileExists('file.txt') then begin
  s2:='';
  len:=0;
      Reset(f);

      while (not EOF(f)) do begin

       Read(f, s);
       i:=1;
       while i<=length(s)+1 do begin
       if s[i]<>' ' then begin
           s2:= s2+(s[i]);
           len:=len+1;
           i:=i+1;
           end
       else begin
       listbox1.items.add(s2 + ', длина = ' + inttostr(length(s2)));
       len:=0;
       s2:='';
       i:=i+1;
       end;
       if i=length(s)+1 then begin
          listbox1.items.add(s2 + ', длина = ' + inttostr(length(s2)));
       end;

      end;
      end;
  closefile(f);
  end;


end;

end.

