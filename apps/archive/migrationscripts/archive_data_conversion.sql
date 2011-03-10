-- we assume that prior to running this, the database structure is all up to date (syncdb'd and migrate'd)

-- START: urbis data
-- import the archive data in temporary tables. stage it up basically
\. stage_up_urbis_archive_data.sql

-- first fix up some shitty data from textpattern
update tmp_textpattern set Category1 = 'mag-article' where ID in (275,276,284,299,281,283,298);

-- just grab the row for the architecture australia magazine and whack it in the publications_magazine table
insert ignore into publications_magazine set title='Urbis', slug='urbis', show_issues = 1;

-- seed the magazine section table with what was known as article types in the old system
insert into articles_magazinesection values (1, 'Comment'), (2, 'Features'), (3, 'Radar'), (4, 'Articles');;

-- generate issues for urbis
insert into publications_magazineissue
(
    magazine_id,
    issue_name,
    slug,
    issue_number,
    issue_volume,
    _order,
    cover_image
)
select
    (select id from publications_magazine where slug = 'urbis'),
    Category2,
    lower(Category2),
    substr(Category2, -2),
    substr(Category2, -2),
    0,
    concat('files/archive/urbis/covers/', substr(Category2, -2), '.jpg')
from
    tmp_textpattern
where
    Category1 in ('mag-article', 'mag-dispatch')
group by
    Category2;

-- populate articles for urbis
-- temporarily change the pk to auto increment
alter table archive_article modify column id int(11) not null auto_increment;
insert into archive_article
(
    title,
    slug,
    content,
    magazine_section_id,
    introduction,
    issue_id
)
select
   tmp.title,
   tmp.title,
   tmp.Body_Html,
   (select id from articles_magazinesection where section_name ='Articles'),
   tmp.Excerpt_Html,
   (select id from publications_magazineissue where slug=tmp.Category2)
from
    tmp_textpattern tmp
where
    tmp.Category1 in ('mag-article', 'mag-dispatch');
alter table archive_article modify column id int(11) not null;

-- get rid of these tags
update archive_article
set
    content = replace(content, '<txp:if_individual_article>','');
update archive_article
set
    content = replace(content, '</txp:if_individual_article>','');

-- replace these with img tags
update archive_article
set
    content = replace(content, '<txp:upm_image image_id="', '<img src="');
update archive_article
set
    content = replace(content, '" form="upm_img_popper"', '"');
update archive_article
set
    content = replace(content, '<txp:thumbnail id="','<img src="');

-- now run some poor mans replacement for doing this recex...some generated sql
update archive_article set content = replace(content, '<img src="1"', '<img src="/site_media/media/files/archive/urbis/images/1.gif"');
update archive_article set content = replace(content, '<img src="2"', '<img src="/site_media/media/files/archive/urbis/images/2.jpg"');
update archive_article set content = replace(content, '<img src="3"', '<img src="/site_media/media/files/archive/urbis/images/3.jpg"');
update archive_article set content = replace(content, '<img src="4"', '<img src="/site_media/media/files/archive/urbis/images/4.jpg"');
update archive_article set content = replace(content, '<img src="5"', '<img src="/site_media/media/files/archive/urbis/images/5.jpg"');
update archive_article set content = replace(content, '<img src="6"', '<img src="/site_media/media/files/archive/urbis/images/6.jpg"');
update archive_article set content = replace(content, '<img src="7"', '<img src="/site_media/media/files/archive/urbis/images/7.jpg"');
update archive_article set content = replace(content, '<img src="8"', '<img src="/site_media/media/files/archive/urbis/images/8.jpg"');
update archive_article set content = replace(content, '<img src="9"', '<img src="/site_media/media/files/archive/urbis/images/9.jpg"');
update archive_article set content = replace(content, '<img src="10"', '<img src="/site_media/media/files/archive/urbis/images/10.jpg"');
update archive_article set content = replace(content, '<img src="11"', '<img src="/site_media/media/files/archive/urbis/images/11.jpg"');
update archive_article set content = replace(content, '<img src="12"', '<img src="/site_media/media/files/archive/urbis/images/12.jpg"');
update archive_article set content = replace(content, '<img src="13"', '<img src="/site_media/media/files/archive/urbis/images/13.jpg"');
update archive_article set content = replace(content, '<img src="14"', '<img src="/site_media/media/files/archive/urbis/images/14.jpg"');
update archive_article set content = replace(content, '<img src="15"', '<img src="/site_media/media/files/archive/urbis/images/15.gif"');
update archive_article set content = replace(content, '<img src="16"', '<img src="/site_media/media/files/archive/urbis/images/16.jpg"');
update archive_article set content = replace(content, '<img src="17"', '<img src="/site_media/media/files/archive/urbis/images/17.gif"');
update archive_article set content = replace(content, '<img src="18"', '<img src="/site_media/media/files/archive/urbis/images/18.jpg"');
update archive_article set content = replace(content, '<img src="19"', '<img src="/site_media/media/files/archive/urbis/images/19.jpg"');
update archive_article set content = replace(content, '<img src="20"', '<img src="/site_media/media/files/archive/urbis/images/20.jpg"');
update archive_article set content = replace(content, '<img src="21"', '<img src="/site_media/media/files/archive/urbis/images/21.jpg"');
update archive_article set content = replace(content, '<img src="22"', '<img src="/site_media/media/files/archive/urbis/images/22.jpg"');
update archive_article set content = replace(content, '<img src="23"', '<img src="/site_media/media/files/archive/urbis/images/23.jpg"');
update archive_article set content = replace(content, '<img src="24"', '<img src="/site_media/media/files/archive/urbis/images/24.jpg"');
update archive_article set content = replace(content, '<img src="25"', '<img src="/site_media/media/files/archive/urbis/images/25.jpg"');
update archive_article set content = replace(content, '<img src="26"', '<img src="/site_media/media/files/archive/urbis/images/26.jpg"');
update archive_article set content = replace(content, '<img src="27"', '<img src="/site_media/media/files/archive/urbis/images/27.jpg"');
update archive_article set content = replace(content, '<img src="28"', '<img src="/site_media/media/files/archive/urbis/images/28.gif"');
update archive_article set content = replace(content, '<img src="29"', '<img src="/site_media/media/files/archive/urbis/images/29.gif"');
update archive_article set content = replace(content, '<img src="30"', '<img src="/site_media/media/files/archive/urbis/images/30.jpg"');
update archive_article set content = replace(content, '<img src="31"', '<img src="/site_media/media/files/archive/urbis/images/31.gif"');
update archive_article set content = replace(content, '<img src="32"', '<img src="/site_media/media/files/archive/urbis/images/32.gif"');
update archive_article set content = replace(content, '<img src="33"', '<img src="/site_media/media/files/archive/urbis/images/33.gif"');
update archive_article set content = replace(content, '<img src="34"', '<img src="/site_media/media/files/archive/urbis/images/34.jpg"');
update archive_article set content = replace(content, '<img src="35"', '<img src="/site_media/media/files/archive/urbis/images/35.jpg"');
update archive_article set content = replace(content, '<img src="36"', '<img src="/site_media/media/files/archive/urbis/images/36.jpg"');
update archive_article set content = replace(content, '<img src="37"', '<img src="/site_media/media/files/archive/urbis/images/37.jpg"');
update archive_article set content = replace(content, '<img src="38"', '<img src="/site_media/media/files/archive/urbis/images/38.jpg"');
update archive_article set content = replace(content, '<img src="39"', '<img src="/site_media/media/files/archive/urbis/images/39.jpg"');
update archive_article set content = replace(content, '<img src="40"', '<img src="/site_media/media/files/archive/urbis/images/40.jpg"');
update archive_article set content = replace(content, '<img src="41"', '<img src="/site_media/media/files/archive/urbis/images/41.jpg"');
update archive_article set content = replace(content, '<img src="42"', '<img src="/site_media/media/files/archive/urbis/images/42.jpg"');
update archive_article set content = replace(content, '<img src="43"', '<img src="/site_media/media/files/archive/urbis/images/43.jpg"');
update archive_article set content = replace(content, '<img src="44"', '<img src="/site_media/media/files/archive/urbis/images/44.jpg"');
update archive_article set content = replace(content, '<img src="45"', '<img src="/site_media/media/files/archive/urbis/images/45.jpg"');
update archive_article set content = replace(content, '<img src="46"', '<img src="/site_media/media/files/archive/urbis/images/46.jpg"');
update archive_article set content = replace(content, '<img src="47"', '<img src="/site_media/media/files/archive/urbis/images/47.jpg"');
update archive_article set content = replace(content, '<img src="48"', '<img src="/site_media/media/files/archive/urbis/images/48.jpg"');
update archive_article set content = replace(content, '<img src="49"', '<img src="/site_media/media/files/archive/urbis/images/49.jpg"');
update archive_article set content = replace(content, '<img src="50"', '<img src="/site_media/media/files/archive/urbis/images/50.jpg"');
update archive_article set content = replace(content, '<img src="51"', '<img src="/site_media/media/files/archive/urbis/images/51.jpg"');
update archive_article set content = replace(content, '<img src="52"', '<img src="/site_media/media/files/archive/urbis/images/52.jpg"');
update archive_article set content = replace(content, '<img src="53"', '<img src="/site_media/media/files/archive/urbis/images/53.jpg"');
update archive_article set content = replace(content, '<img src="54"', '<img src="/site_media/media/files/archive/urbis/images/54.jpg"');
update archive_article set content = replace(content, '<img src="55"', '<img src="/site_media/media/files/archive/urbis/images/55.jpg"');
update archive_article set content = replace(content, '<img src="56"', '<img src="/site_media/media/files/archive/urbis/images/56.jpg"');
update archive_article set content = replace(content, '<img src="57"', '<img src="/site_media/media/files/archive/urbis/images/57.jpg"');
update archive_article set content = replace(content, '<img src="58"', '<img src="/site_media/media/files/archive/urbis/images/58.jpg"');
update archive_article set content = replace(content, '<img src="59"', '<img src="/site_media/media/files/archive/urbis/images/59.jpg"');
update archive_article set content = replace(content, '<img src="60"', '<img src="/site_media/media/files/archive/urbis/images/60.jpg"');
update archive_article set content = replace(content, '<img src="61"', '<img src="/site_media/media/files/archive/urbis/images/61.jpg"');
update archive_article set content = replace(content, '<img src="62"', '<img src="/site_media/media/files/archive/urbis/images/62.jpg"');
update archive_article set content = replace(content, '<img src="63"', '<img src="/site_media/media/files/archive/urbis/images/63.jpg"');
update archive_article set content = replace(content, '<img src="64"', '<img src="/site_media/media/files/archive/urbis/images/64.jpg"');
update archive_article set content = replace(content, '<img src="65"', '<img src="/site_media/media/files/archive/urbis/images/65.jpg"');
update archive_article set content = replace(content, '<img src="66"', '<img src="/site_media/media/files/archive/urbis/images/66.jpg"');
update archive_article set content = replace(content, '<img src="67"', '<img src="/site_media/media/files/archive/urbis/images/67.jpg"');
update archive_article set content = replace(content, '<img src="79"', '<img src="/site_media/media/files/archive/urbis/images/79.jpg"');
update archive_article set content = replace(content, '<img src="78"', '<img src="/site_media/media/files/archive/urbis/images/78.jpg"');
update archive_article set content = replace(content, '<img src="70"', '<img src="/site_media/media/files/archive/urbis/images/70.jpg"');
update archive_article set content = replace(content, '<img src="71"', '<img src="/site_media/media/files/archive/urbis/images/71.jpg"');
update archive_article set content = replace(content, '<img src="72"', '<img src="/site_media/media/files/archive/urbis/images/72.jpg"');
update archive_article set content = replace(content, '<img src="73"', '<img src="/site_media/media/files/archive/urbis/images/73.jpg"');
update archive_article set content = replace(content, '<img src="74"', '<img src="/site_media/media/files/archive/urbis/images/74.jpg"');
update archive_article set content = replace(content, '<img src="75"', '<img src="/site_media/media/files/archive/urbis/images/75.jpg"');
update archive_article set content = replace(content, '<img src="80"', '<img src="/site_media/media/files/archive/urbis/images/80.jpg"');
update archive_article set content = replace(content, '<img src="76"', '<img src="/site_media/media/files/archive/urbis/images/76.jpg"');
update archive_article set content = replace(content, '<img src="81"', '<img src="/site_media/media/files/archive/urbis/images/81.jpg"');
update archive_article set content = replace(content, '<img src="82"', '<img src="/site_media/media/files/archive/urbis/images/82.jpg"');
update archive_article set content = replace(content, '<img src="83"', '<img src="/site_media/media/files/archive/urbis/images/83.jpg"');
update archive_article set content = replace(content, '<img src="84"', '<img src="/site_media/media/files/archive/urbis/images/84.jpg"');
update archive_article set content = replace(content, '<img src="85"', '<img src="/site_media/media/files/archive/urbis/images/85.jpg"');
update archive_article set content = replace(content, '<img src="86"', '<img src="/site_media/media/files/archive/urbis/images/86.jpg"');
update archive_article set content = replace(content, '<img src="87"', '<img src="/site_media/media/files/archive/urbis/images/87.jpg"');
update archive_article set content = replace(content, '<img src="88"', '<img src="/site_media/media/files/archive/urbis/images/88.jpg"');
update archive_article set content = replace(content, '<img src="89"', '<img src="/site_media/media/files/archive/urbis/images/89.jpg"');
update archive_article set content = replace(content, '<img src="90"', '<img src="/site_media/media/files/archive/urbis/images/90.gif"');
update archive_article set content = replace(content, '<img src="91"', '<img src="/site_media/media/files/archive/urbis/images/91.gif"');
update archive_article set content = replace(content, '<img src="93"', '<img src="/site_media/media/files/archive/urbis/images/93.gif"');
update archive_article set content = replace(content, '<img src="94"', '<img src="/site_media/media/files/archive/urbis/images/94.gif"');
update archive_article set content = replace(content, '<img src="95"', '<img src="/site_media/media/files/archive/urbis/images/95.gif"');
update archive_article set content = replace(content, '<img src="96"', '<img src="/site_media/media/files/archive/urbis/images/96.gif"');
update archive_article set content = replace(content, '<img src="97"', '<img src="/site_media/media/files/archive/urbis/images/97.gif"');
update archive_article set content = replace(content, '<img src="98"', '<img src="/site_media/media/files/archive/urbis/images/98.gif"');
update archive_article set content = replace(content, '<img src="99"', '<img src="/site_media/media/files/archive/urbis/images/99.gif"');
update archive_article set content = replace(content, '<img src="100"', '<img src="/site_media/media/files/archive/urbis/images/100.gif"');
update archive_article set content = replace(content, '<img src="101"', '<img src="/site_media/media/files/archive/urbis/images/101.gif"');
update archive_article set content = replace(content, '<img src="102"', '<img src="/site_media/media/files/archive/urbis/images/102.gif"');
update archive_article set content = replace(content, '<img src="103"', '<img src="/site_media/media/files/archive/urbis/images/103.gif"');
update archive_article set content = replace(content, '<img src="104"', '<img src="/site_media/media/files/archive/urbis/images/104.gif"');
update archive_article set content = replace(content, '<img src="105"', '<img src="/site_media/media/files/archive/urbis/images/105.gif"');
update archive_article set content = replace(content, '<img src="106"', '<img src="/site_media/media/files/archive/urbis/images/106.gif"');
update archive_article set content = replace(content, '<img src="107"', '<img src="/site_media/media/files/archive/urbis/images/107.gif"');
update archive_article set content = replace(content, '<img src="108"', '<img src="/site_media/media/files/archive/urbis/images/108.gif"');
update archive_article set content = replace(content, '<img src="109"', '<img src="/site_media/media/files/archive/urbis/images/109.jpg"');
update archive_article set content = replace(content, '<img src="111"', '<img src="/site_media/media/files/archive/urbis/images/111.jpg"');
update archive_article set content = replace(content, '<img src="112"', '<img src="/site_media/media/files/archive/urbis/images/112.jpg"');
update archive_article set content = replace(content, '<img src="113"', '<img src="/site_media/media/files/archive/urbis/images/113.jpg"');
update archive_article set content = replace(content, '<img src="120"', '<img src="/site_media/media/files/archive/urbis/images/120.jpg"');
update archive_article set content = replace(content, '<img src="115"', '<img src="/site_media/media/files/archive/urbis/images/115.jpg"');
update archive_article set content = replace(content, '<img src="134"', '<img src="/site_media/media/files/archive/urbis/images/134.jpg"');
update archive_article set content = replace(content, '<img src="117"', '<img src="/site_media/media/files/archive/urbis/images/117.jpg"');
update archive_article set content = replace(content, '<img src="118"', '<img src="/site_media/media/files/archive/urbis/images/118.jpg"');
update archive_article set content = replace(content, '<img src="121"', '<img src="/site_media/media/files/archive/urbis/images/121.jpg"');
update archive_article set content = replace(content, '<img src="122"', '<img src="/site_media/media/files/archive/urbis/images/122.jpg"');
update archive_article set content = replace(content, '<img src="123"', '<img src="/site_media/media/files/archive/urbis/images/123.jpg"');
update archive_article set content = replace(content, '<img src="124"', '<img src="/site_media/media/files/archive/urbis/images/124.jpg"');
update archive_article set content = replace(content, '<img src="125"', '<img src="/site_media/media/files/archive/urbis/images/125.jpg"');
update archive_article set content = replace(content, '<img src="126"', '<img src="/site_media/media/files/archive/urbis/images/126.jpg"');
update archive_article set content = replace(content, '<img src="127"', '<img src="/site_media/media/files/archive/urbis/images/127.jpg"');
update archive_article set content = replace(content, '<img src="128"', '<img src="/site_media/media/files/archive/urbis/images/128.jpg"');
update archive_article set content = replace(content, '<img src="129"', '<img src="/site_media/media/files/archive/urbis/images/129.jpg"');
update archive_article set content = replace(content, '<img src="130"', '<img src="/site_media/media/files/archive/urbis/images/130.jpg"');
update archive_article set content = replace(content, '<img src="131"', '<img src="/site_media/media/files/archive/urbis/images/131.jpg"');
update archive_article set content = replace(content, '<img src="132"', '<img src="/site_media/media/files/archive/urbis/images/132.jpg"');
update archive_article set content = replace(content, '<img src="133"', '<img src="/site_media/media/files/archive/urbis/images/133.jpg"');
update archive_article set content = replace(content, '<img src="135"', '<img src="/site_media/media/files/archive/urbis/images/135.jpg"');
update archive_article set content = replace(content, '<img src="136"', '<img src="/site_media/media/files/archive/urbis/images/136.jpg"');
update archive_article set content = replace(content, '<img src="137"', '<img src="/site_media/media/files/archive/urbis/images/137.jpg"');
update archive_article set content = replace(content, '<img src="138"', '<img src="/site_media/media/files/archive/urbis/images/138.gif"');
update archive_article set content = replace(content, '<img src="139"', '<img src="/site_media/media/files/archive/urbis/images/139.gif"');
update archive_article set content = replace(content, '<img src="140"', '<img src="/site_media/media/files/archive/urbis/images/140.jpg"');
update archive_article set content = replace(content, '<img src="141"', '<img src="/site_media/media/files/archive/urbis/images/141.jpg"');
update archive_article set content = replace(content, '<img src="142"', '<img src="/site_media/media/files/archive/urbis/images/142.jpg"');
update archive_article set content = replace(content, '<img src="143"', '<img src="/site_media/media/files/archive/urbis/images/143.jpg"');
update archive_article set content = replace(content, '<img src="144"', '<img src="/site_media/media/files/archive/urbis/images/144.jpg"');
update archive_article set content = replace(content, '<img src="145"', '<img src="/site_media/media/files/archive/urbis/images/145.jpg"');
update archive_article set content = replace(content, '<img src="146"', '<img src="/site_media/media/files/archive/urbis/images/146.jpg"');
update archive_article set content = replace(content, '<img src="147"', '<img src="/site_media/media/files/archive/urbis/images/147.jpg"');
update archive_article set content = replace(content, '<img src="148"', '<img src="/site_media/media/files/archive/urbis/images/148.jpg"');
update archive_article set content = replace(content, '<img src="149"', '<img src="/site_media/media/files/archive/urbis/images/149.jpg"');
update archive_article set content = replace(content, '<img src="150"', '<img src="/site_media/media/files/archive/urbis/images/150.jpg"');
update archive_article set content = replace(content, '<img src="151"', '<img src="/site_media/media/files/archive/urbis/images/151.jpg"');
update archive_article set content = replace(content, '<img src="152"', '<img src="/site_media/media/files/archive/urbis/images/152.jpg"');
update archive_article set content = replace(content, '<img src="153"', '<img src="/site_media/media/files/archive/urbis/images/153.jpg"');
update archive_article set content = replace(content, '<img src="154"', '<img src="/site_media/media/files/archive/urbis/images/154.jpg"');
update archive_article set content = replace(content, '<img src="155"', '<img src="/site_media/media/files/archive/urbis/images/155.jpg"');
update archive_article set content = replace(content, '<img src="162"', '<img src="/site_media/media/files/archive/urbis/images/162.jpg"');
update archive_article set content = replace(content, '<img src="160"', '<img src="/site_media/media/files/archive/urbis/images/160.jpg"');
update archive_article set content = replace(content, '<img src="158"', '<img src="/site_media/media/files/archive/urbis/images/158.jpg"');
update archive_article set content = replace(content, '<img src="163"', '<img src="/site_media/media/files/archive/urbis/images/163.jpg"');
update archive_article set content = replace(content, '<img src="164"', '<img src="/site_media/media/files/archive/urbis/images/164.jpg"');
update archive_article set content = replace(content, '<img src="165"', '<img src="/site_media/media/files/archive/urbis/images/165.jpg"');
update archive_article set content = replace(content, '<img src="166"', '<img src="/site_media/media/files/archive/urbis/images/166.jpg"');
update archive_article set content = replace(content, '<img src="167"', '<img src="/site_media/media/files/archive/urbis/images/167.jpg"');
update archive_article set content = replace(content, '<img src="168"', '<img src="/site_media/media/files/archive/urbis/images/168.jpg"');
update archive_article set content = replace(content, '<img src="169"', '<img src="/site_media/media/files/archive/urbis/images/169.jpg"');
update archive_article set content = replace(content, '<img src="170"', '<img src="/site_media/media/files/archive/urbis/images/170.jpg"');
update archive_article set content = replace(content, '<img src="171"', '<img src="/site_media/media/files/archive/urbis/images/171.jpg"');
update archive_article set content = replace(content, '<img src="172"', '<img src="/site_media/media/files/archive/urbis/images/172.jpg"');
update archive_article set content = replace(content, '<img src="176"', '<img src="/site_media/media/files/archive/urbis/images/176.jpg"');
update archive_article set content = replace(content, '<img src="175"', '<img src="/site_media/media/files/archive/urbis/images/175.jpg"');
update archive_article set content = replace(content, '<img src="177"', '<img src="/site_media/media/files/archive/urbis/images/177.jpg"');
update archive_article set content = replace(content, '<img src="178"', '<img src="/site_media/media/files/archive/urbis/images/178.jpg"');
update archive_article set content = replace(content, '<img src="179"', '<img src="/site_media/media/files/archive/urbis/images/179.jpg"');
update archive_article set content = replace(content, '<img src="180"', '<img src="/site_media/media/files/archive/urbis/images/180.jpg"');
update archive_article set content = replace(content, '<img src="181"', '<img src="/site_media/media/files/archive/urbis/images/181.jpg"');
update archive_article set content = replace(content, '<img src="182"', '<img src="/site_media/media/files/archive/urbis/images/182.jpg"');
update archive_article set content = replace(content, '<img src="183"', '<img src="/site_media/media/files/archive/urbis/images/183.jpg"');
update archive_article set content = replace(content, '<img src="184"', '<img src="/site_media/media/files/archive/urbis/images/184.jpg"');
update archive_article set content = replace(content, '<img src="185"', '<img src="/site_media/media/files/archive/urbis/images/185.jpg"');
update archive_article set content = replace(content, '<img src="188"', '<img src="/site_media/media/files/archive/urbis/images/188.jpg"');
update archive_article set content = replace(content, '<img src="195"', '<img src="/site_media/media/files/archive/urbis/images/195.jpg"');
update archive_article set content = replace(content, '<img src="189"', '<img src="/site_media/media/files/archive/urbis/images/189.jpg"');
update archive_article set content = replace(content, '<img src="192"', '<img src="/site_media/media/files/archive/urbis/images/192.jpg"');
update archive_article set content = replace(content, '<img src="191"', '<img src="/site_media/media/files/archive/urbis/images/191.jpg"');
update archive_article set content = replace(content, '<img src="193"', '<img src="/site_media/media/files/archive/urbis/images/193.jpg"');
update archive_article set content = replace(content, '<img src="194"', '<img src="/site_media/media/files/archive/urbis/images/194.jpg"');
update archive_article set content = replace(content, '<img src="196"', '<img src="/site_media/media/files/archive/urbis/images/196.jpg"');
update archive_article set content = replace(content, '<img src="197"', '<img src="/site_media/media/files/archive/urbis/images/197.jpg"');
update archive_article set content = replace(content, '<img src="198"', '<img src="/site_media/media/files/archive/urbis/images/198.jpg"');
update archive_article set content = replace(content, '<img src="201"', '<img src="/site_media/media/files/archive/urbis/images/201.jpg"');
update archive_article set content = replace(content, '<img src="200"', '<img src="/site_media/media/files/archive/urbis/images/200.jpg"');
update archive_article set content = replace(content, '<img src="206"', '<img src="/site_media/media/files/archive/urbis/images/206.jpg"');
update archive_article set content = replace(content, '<img src="207"', '<img src="/site_media/media/files/archive/urbis/images/207.jpg"');
update archive_article set content = replace(content, '<img src="208"', '<img src="/site_media/media/files/archive/urbis/images/208.jpg"');
update archive_article set content = replace(content, '<img src="209"', '<img src="/site_media/media/files/archive/urbis/images/209.jpg"');
update archive_article set content = replace(content, '<img src="214"', '<img src="/site_media/media/files/archive/urbis/images/214.jpg"');
update archive_article set content = replace(content, '<img src="213"', '<img src="/site_media/media/files/archive/urbis/images/213.jpg"');
update archive_article set content = replace(content, '<img src="212"', '<img src="/site_media/media/files/archive/urbis/images/212.jpg"');
update archive_article set content = replace(content, '<img src="215"', '<img src="/site_media/media/files/archive/urbis/images/215.jpg"');
update archive_article set content = replace(content, '<img src="225"', '<img src="/site_media/media/files/archive/urbis/images/225.jpg"');
update archive_article set content = replace(content, '<img src="220"', '<img src="/site_media/media/files/archive/urbis/images/220.jpg"');
update archive_article set content = replace(content, '<img src="224"', '<img src="/site_media/media/files/archive/urbis/images/224.jpg"');
update archive_article set content = replace(content, '<img src="226"', '<img src="/site_media/media/files/archive/urbis/images/226.jpg"');
update archive_article set content = replace(content, '<img src="231"', '<img src="/site_media/media/files/archive/urbis/images/231.jpg"');
update archive_article set content = replace(content, '<img src="228"', '<img src="/site_media/media/files/archive/urbis/images/228.jpg"');
update archive_article set content = replace(content, '<img src="230"', '<img src="/site_media/media/files/archive/urbis/images/230.jpg"');
update archive_article set content = replace(content, '<img src="232"', '<img src="/site_media/media/files/archive/urbis/images/232.jpg"');
update archive_article set content = replace(content, '<img src="240"', '<img src="/site_media/media/files/archive/urbis/images/240.jpg"');
update archive_article set content = replace(content, '<img src="239"', '<img src="/site_media/media/files/archive/urbis/images/239.jpg"');
update archive_article set content = replace(content, '<img src="238"', '<img src="/site_media/media/files/archive/urbis/images/238.jpg"');
update archive_article set content = replace(content, '<img src="236"', '<img src="/site_media/media/files/archive/urbis/images/236.jpg"');
update archive_article set content = replace(content, '<img src="237"', '<img src="/site_media/media/files/archive/urbis/images/237.jpg"');
update archive_article set content = replace(content, '<img src="241"', '<img src="/site_media/media/files/archive/urbis/images/241.jpg"');
update archive_article set content = replace(content, '<img src="242"', '<img src="/site_media/media/files/archive/urbis/images/242.jpg"');
update archive_article set content = replace(content, '<img src="243"', '<img src="/site_media/media/files/archive/urbis/images/243.jpg"');
update archive_article set content = replace(content, '<img src="244"', '<img src="/site_media/media/files/archive/urbis/images/244.jpg"');
update archive_article set content = replace(content, '<img src="245"', '<img src="/site_media/media/files/archive/urbis/images/245.jpg"');
update archive_article set content = replace(content, '<img src="246"', '<img src="/site_media/media/files/archive/urbis/images/246.jpg"');
update archive_article set content = replace(content, '<img src="247"', '<img src="/site_media/media/files/archive/urbis/images/247.jpg"');
update archive_article set content = replace(content, '<img src="248"', '<img src="/site_media/media/files/archive/urbis/images/248.jpg"');
update archive_article set content = replace(content, '<img src="254"', '<img src="/site_media/media/files/archive/urbis/images/254.jpg"');
update archive_article set content = replace(content, '<img src="250"', '<img src="/site_media/media/files/archive/urbis/images/250.jpg"');
update archive_article set content = replace(content, '<img src="251"', '<img src="/site_media/media/files/archive/urbis/images/251.jpg"');
update archive_article set content = replace(content, '<img src="252"', '<img src="/site_media/media/files/archive/urbis/images/252.jpg"');
update archive_article set content = replace(content, '<img src="262"', '<img src="/site_media/media/files/archive/urbis/images/262.jpg"');
update archive_article set content = replace(content, '<img src="257"', '<img src="/site_media/media/files/archive/urbis/images/257.jpg"');
update archive_article set content = replace(content, '<img src="260"', '<img src="/site_media/media/files/archive/urbis/images/260.jpg"');
update archive_article set content = replace(content, '<img src="259"', '<img src="/site_media/media/files/archive/urbis/images/259.jpg"');
update archive_article set content = replace(content, '<img src="261"', '<img src="/site_media/media/files/archive/urbis/images/261.jpg"');
update archive_article set content = replace(content, '<img src="263"', '<img src="/site_media/media/files/archive/urbis/images/263.jpg"');
update archive_article set content = replace(content, '<img src="264"', '<img src="/site_media/media/files/archive/urbis/images/264.jpg"');
update archive_article set content = replace(content, '<img src="265"', '<img src="/site_media/media/files/archive/urbis/images/265.jpg"');
update archive_article set content = replace(content, '<img src="266"', '<img src="/site_media/media/files/archive/urbis/images/266.jpg"');
update archive_article set content = replace(content, '<img src="267"', '<img src="/site_media/media/files/archive/urbis/images/267.jpg"');
update archive_article set content = replace(content, '<img src="268"', '<img src="/site_media/media/files/archive/urbis/images/268.jpg"');
update archive_article set content = replace(content, '<img src="269"', '<img src="/site_media/media/files/archive/urbis/images/269.jpg"');
update archive_article set content = replace(content, '<img src="270"', '<img src="/site_media/media/files/archive/urbis/images/270.jpg"');
update archive_article set content = replace(content, '<img src="271"', '<img src="/site_media/media/files/archive/urbis/images/271.jpg"');
update archive_article set content = replace(content, '<img src="272"', '<img src="/site_media/media/files/archive/urbis/images/272.jpg"');
update archive_article set content = replace(content, '<img src="274"', '<img src="/site_media/media/files/archive/urbis/images/274.jpg"');
update archive_article set content = replace(content, '<img src="275"', '<img src="/site_media/media/files/archive/urbis/images/275.jpg"');
update archive_article set content = replace(content, '<img src="276"', '<img src="/site_media/media/files/archive/urbis/images/276.jpg"');
update archive_article set content = replace(content, '<img src="277"', '<img src="/site_media/media/files/archive/urbis/images/277.jpg"');
update archive_article set content = replace(content, '<img src="278"', '<img src="/site_media/media/files/archive/urbis/images/278.jpg"');
update archive_article set content = replace(content, '<img src="279"', '<img src="/site_media/media/files/archive/urbis/images/279.jpg"');
update archive_article set content = replace(content, '<img src="280"', '<img src="/site_media/media/files/archive/urbis/images/280.jpg"');
update archive_article set content = replace(content, '<img src="281"', '<img src="/site_media/media/files/archive/urbis/images/281.jpg"');
update archive_article set content = replace(content, '<img src="282"', '<img src="/site_media/media/files/archive/urbis/images/282.jpg"');
update archive_article set content = replace(content, '<img src="283"', '<img src="/site_media/media/files/archive/urbis/images/283.jpg"');
update archive_article set content = replace(content, '<img src="284"', '<img src="/site_media/media/files/archive/urbis/images/284.jpg"');
update archive_article set content = replace(content, '<img src="285"', '<img src="/site_media/media/files/archive/urbis/images/285.jpg"');
update archive_article set content = replace(content, '<img src="286"', '<img src="/site_media/media/files/archive/urbis/images/286.jpg"');
update archive_article set content = replace(content, '<img src="287"', '<img src="/site_media/media/files/archive/urbis/images/287.jpg"');
update archive_article set content = replace(content, '<img src="288"', '<img src="/site_media/media/files/archive/urbis/images/288.jpg"');
update archive_article set content = replace(content, '<img src="289"', '<img src="/site_media/media/files/archive/urbis/images/289.jpg"');
update archive_article set content = replace(content, '<img src="290"', '<img src="/site_media/media/files/archive/urbis/images/290.jpg"');
update archive_article set content = replace(content, '<img src="291"', '<img src="/site_media/media/files/archive/urbis/images/291.jpg"');
update archive_article set content = replace(content, '<img src="292"', '<img src="/site_media/media/files/archive/urbis/images/292.jpg"');
update archive_article set content = replace(content, '<img src="293"', '<img src="/site_media/media/files/archive/urbis/images/293.jpg"');
update archive_article set content = replace(content, '<img src="294"', '<img src="/site_media/media/files/archive/urbis/images/294.jpg"');
update archive_article set content = replace(content, '<img src="295"', '<img src="/site_media/media/files/archive/urbis/images/295.jpg"');
update archive_article set content = replace(content, '<img src="301"', '<img src="/site_media/media/files/archive/urbis/images/301.jpg"');
update archive_article set content = replace(content, '<img src="297"', '<img src="/site_media/media/files/archive/urbis/images/297.jpg"');
update archive_article set content = replace(content, '<img src="298"', '<img src="/site_media/media/files/archive/urbis/images/298.jpg"');
update archive_article set content = replace(content, '<img src="299"', '<img src="/site_media/media/files/archive/urbis/images/299.jpg"');
update archive_article set content = replace(content, '<img src="300"', '<img src="/site_media/media/files/archive/urbis/images/300.jpg"');
update archive_article set content = replace(content, '<img src="302"', '<img src="/site_media/media/files/archive/urbis/images/302.jpg"');
update archive_article set content = replace(content, '<img src="303"', '<img src="/site_media/media/files/archive/urbis/images/303.jpg"');
update archive_article set content = replace(content, '<img src="304"', '<img src="/site_media/media/files/archive/urbis/images/304.jpg"');
update archive_article set content = replace(content, '<img src="305"', '<img src="/site_media/media/files/archive/urbis/images/305.jpg"');
update archive_article set content = replace(content, '<img src="306"', '<img src="/site_media/media/files/archive/urbis/images/306.jpg"');
update archive_article set content = replace(content, '<img src="307"', '<img src="/site_media/media/files/archive/urbis/images/307.jpg"');
update archive_article set content = replace(content, '<img src="308"', '<img src="/site_media/media/files/archive/urbis/images/308.jpg"');
update archive_article set content = replace(content, '<img src="309"', '<img src="/site_media/media/files/archive/urbis/images/309.jpg"');
update archive_article set content = replace(content, '<img src="310"', '<img src="/site_media/media/files/archive/urbis/images/310.jpg"');
update archive_article set content = replace(content, '<img src="311"', '<img src="/site_media/media/files/archive/urbis/images/311.jpg"');
update archive_article set content = replace(content, '<img src="312"', '<img src="/site_media/media/files/archive/urbis/images/312.jpg"');
update archive_article set content = replace(content, '<img src="313"', '<img src="/site_media/media/files/archive/urbis/images/313.jpg"');
update archive_article set content = replace(content, '<img src="314"', '<img src="/site_media/media/files/archive/urbis/images/314.jpg"');
update archive_article set content = replace(content, '<img src="315"', '<img src="/site_media/media/files/archive/urbis/images/315.jpg"');
update archive_article set content = replace(content, '<img src="316"', '<img src="/site_media/media/files/archive/urbis/images/316.jpg"');
update archive_article set content = replace(content, '<img src="317"', '<img src="/site_media/media/files/archive/urbis/images/317.jpg"');
update archive_article set content = replace(content, '<img src="318"', '<img src="/site_media/media/files/archive/urbis/images/318.jpg"');
update archive_article set content = replace(content, '<img src="319"', '<img src="/site_media/media/files/archive/urbis/images/319.jpg"');
update archive_article set content = replace(content, '<img src="320"', '<img src="/site_media/media/files/archive/urbis/images/320.jpg"');
update archive_article set content = replace(content, '<img src="321"', '<img src="/site_media/media/files/archive/urbis/images/321.jpg"');
update archive_article set content = replace(content, '<img src="322"', '<img src="/site_media/media/files/archive/urbis/images/322.jpg"');
update archive_article set content = replace(content, '<img src="325"', '<img src="/site_media/media/files/archive/urbis/images/325.jpg"');
update archive_article set content = replace(content, '<img src="324"', '<img src="/site_media/media/files/archive/urbis/images/324.jpg"');
update archive_article set content = replace(content, '<img src="326"', '<img src="/site_media/media/files/archive/urbis/images/326.jpg"');
update archive_article set content = replace(content, '<img src="327"', '<img src="/site_media/media/files/archive/urbis/images/327.jpg"');
update archive_article set content = replace(content, '<img src="328"', '<img src="/site_media/media/files/archive/urbis/images/328.jpg"');
update archive_article set content = replace(content, '<img src="329"', '<img src="/site_media/media/files/archive/urbis/images/329.jpg"');
update archive_article set content = replace(content, '<img src="333"', '<img src="/site_media/media/files/archive/urbis/images/333.jpg"');
update archive_article set content = replace(content, '<img src="331"', '<img src="/site_media/media/files/archive/urbis/images/331.jpg"');
update archive_article set content = replace(content, '<img src="332"', '<img src="/site_media/media/files/archive/urbis/images/332.jpg"');
update archive_article set content = replace(content, '<img src="334"', '<img src="/site_media/media/files/archive/urbis/images/334.jpg"');
update archive_article set content = replace(content, '<img src="335"', '<img src="/site_media/media/files/archive/urbis/images/335.jpg"');
update archive_article set content = replace(content, '<img src="336"', '<img src="/site_media/media/files/archive/urbis/images/336.jpg"');
update archive_article set content = replace(content, '<img src="337"', '<img src="/site_media/media/files/archive/urbis/images/337.jpg"');
update archive_article set content = replace(content, '<img src="338"', '<img src="/site_media/media/files/archive/urbis/images/338.jpg"');
update archive_article set content = replace(content, '<img src="339"', '<img src="/site_media/media/files/archive/urbis/images/339.jpg"');
update archive_article set content = replace(content, '<img src="340"', '<img src="/site_media/media/files/archive/urbis/images/340.jpg"');
update archive_article set content = replace(content, '<img src="341"', '<img src="/site_media/media/files/archive/urbis/images/341.jpg"');
update archive_article set content = replace(content, '<img src="342"', '<img src="/site_media/media/files/archive/urbis/images/342.jpg"');
update archive_article set content = replace(content, '<img src="343"', '<img src="/site_media/media/files/archive/urbis/images/343.jpg"');
update archive_article set content = replace(content, '<img src="344"', '<img src="/site_media/media/files/archive/urbis/images/344.jpg"');
update archive_article set content = replace(content, '<img src="345"', '<img src="/site_media/media/files/archive/urbis/images/345.jpg"');
update archive_article set content = replace(content, '<img src="346"', '<img src="/site_media/media/files/archive/urbis/images/346.png"');
update archive_article set content = replace(content, '<img src="347"', '<img src="/site_media/media/files/archive/urbis/images/347.jpg"');
update archive_article set content = replace(content, '<img src="348"', '<img src="/site_media/media/files/archive/urbis/images/348.jpg"');
update archive_article set content = replace(content, '<img src="349"', '<img src="/site_media/media/files/archive/urbis/images/349.jpg"');
update archive_article set content = replace(content, '<img src="350"', '<img src="/site_media/media/files/archive/urbis/images/350.jpg"');
update archive_article set content = replace(content, '<img src="351"', '<img src="/site_media/media/files/archive/urbis/images/351.jpg"');
update archive_article set content = replace(content, '<img src="352"', '<img src="/site_media/media/files/archive/urbis/images/352.jpg"');
update archive_article set content = replace(content, '<img src="353"', '<img src="/site_media/media/files/archive/urbis/images/353.jpg"');
update archive_article set content = replace(content, '<img src="354"', '<img src="/site_media/media/files/archive/urbis/images/354.jpg"');
update archive_article set content = replace(content, '<img src="355"', '<img src="/site_media/media/files/archive/urbis/images/355.jpg"');
update archive_article set content = replace(content, '<img src="356"', '<img src="/site_media/media/files/archive/urbis/images/356.jpg"');
update archive_article set content = replace(content, '<img src="359"', '<img src="/site_media/media/files/archive/urbis/images/359.jpg"');
update archive_article set content = replace(content, '<img src="358"', '<img src="/site_media/media/files/archive/urbis/images/358.jpg"');
update archive_article set content = replace(content, '<img src="360"', '<img src="/site_media/media/files/archive/urbis/images/360.jpg"');
update archive_article set content = replace(content, '<img src="361"', '<img src="/site_media/media/files/archive/urbis/images/361.jpg"');
update archive_article set content = replace(content, '<img src="362"', '<img src="/site_media/media/files/archive/urbis/images/362.jpg"');
update archive_article set content = replace(content, '<img src="363"', '<img src="/site_media/media/files/archive/urbis/images/363.jpg"');
update archive_article set content = replace(content, '<img src="366"', '<img src="/site_media/media/files/archive/urbis/images/366.jpg"');
update archive_article set content = replace(content, '<img src="365"', '<img src="/site_media/media/files/archive/urbis/images/365.jpg"');
update archive_article set content = replace(content, '<img src="367"', '<img src="/site_media/media/files/archive/urbis/images/367.jpg"');
update archive_article set content = replace(content, '<img src="368"', '<img src="/site_media/media/files/archive/urbis/images/368.jpg"');
update archive_article set content = replace(content, '<img src="369"', '<img src="/site_media/media/files/archive/urbis/images/369.jpg"');
update archive_article set content = replace(content, '<img src="370"', '<img src="/site_media/media/files/archive/urbis/images/370.jpg"');
update archive_article set content = replace(content, '<img src="371"', '<img src="/site_media/media/files/archive/urbis/images/371.jpg"');
update archive_article set content = replace(content, '<img src="372"', '<img src="/site_media/media/files/archive/urbis/images/372.jpg"');
update archive_article set content = replace(content, '<img src="375"', '<img src="/site_media/media/files/archive/urbis/images/375.jpg"');
update archive_article set content = replace(content, '<img src="374"', '<img src="/site_media/media/files/archive/urbis/images/374.jpg"');
update archive_article set content = replace(content, '<img src="384"', '<img src="/site_media/media/files/archive/urbis/images/384.jpg"');
update archive_article set content = replace(content, '<img src="377"', '<img src="/site_media/media/files/archive/urbis/images/377.jpg"');
update archive_article set content = replace(content, '<img src="380"', '<img src="/site_media/media/files/archive/urbis/images/380.jpg"');
update archive_article set content = replace(content, '<img src="379"', '<img src="/site_media/media/files/archive/urbis/images/379.jpg"');
update archive_article set content = replace(content, '<img src="383"', '<img src="/site_media/media/files/archive/urbis/images/383.jpg"');
update archive_article set content = replace(content, '<img src="385"', '<img src="/site_media/media/files/archive/urbis/images/385.jpg"');
update archive_article set content = replace(content, '<img src="386"', '<img src="/site_media/media/files/archive/urbis/images/386.jpg"');
update archive_article set content = replace(content, '<img src="387"', '<img src="/site_media/media/files/archive/urbis/images/387.jpg"');
update archive_article set content = replace(content, '<img src="390"', '<img src="/site_media/media/files/archive/urbis/images/390.jpg"');
update archive_article set content = replace(content, '<img src="389"', '<img src="/site_media/media/files/archive/urbis/images/389.jpg"');
update archive_article set content = replace(content, '<img src="391"', '<img src="/site_media/media/files/archive/urbis/images/391.jpg"');
update archive_article set content = replace(content, '<img src="392"', '<img src="/site_media/media/files/archive/urbis/images/392.jpg"');
update archive_article set content = replace(content, '<img src="393"', '<img src="/site_media/media/files/archive/urbis/images/393.jpg"');
update archive_article set content = replace(content, '<img src="394"', '<img src="/site_media/media/files/archive/urbis/images/394.jpg"');
update archive_article set content = replace(content, '<img src="395"', '<img src="/site_media/media/files/archive/urbis/images/395.jpg"');
update archive_article set content = replace(content, '<img src="396"', '<img src="/site_media/media/files/archive/urbis/images/396.jpg"');
update archive_article set content = replace(content, '<img src="397"', '<img src="/site_media/media/files/archive/urbis/images/397.jpg"');
update archive_article set content = replace(content, '<img src="398"', '<img src="/site_media/media/files/archive/urbis/images/398.jpg"');
update archive_article set content = replace(content, '<img src="399"', '<img src="/site_media/media/files/archive/urbis/images/399.jpg"');
update archive_article set content = replace(content, '<img src="400"', '<img src="/site_media/media/files/archive/urbis/images/400.jpg"');
update archive_article set content = replace(content, '<img src="401"', '<img src="/site_media/media/files/archive/urbis/images/401.jpg"');
update archive_article set content = replace(content, '<img src="402"', '<img src="/site_media/media/files/archive/urbis/images/402.jpg"');
update archive_article set content = replace(content, '<img src="403"', '<img src="/site_media/media/files/archive/urbis/images/403.jpg"');
update archive_article set content = replace(content, '<img src="404"', '<img src="/site_media/media/files/archive/urbis/images/404.jpg"');
update archive_article set content = replace(content, '<img src="405"', '<img src="/site_media/media/files/archive/urbis/images/405.jpg"');
update archive_article set content = replace(content, '<img src="406"', '<img src="/site_media/media/files/archive/urbis/images/406.jpg"');
update archive_article set content = replace(content, '<img src="407"', '<img src="/site_media/media/files/archive/urbis/images/407.jpg"');
update archive_article set content = replace(content, '<img src="408"', '<img src="/site_media/media/files/archive/urbis/images/408.jpg"');
update archive_article set content = replace(content, '<img src="409"', '<img src="/site_media/media/files/archive/urbis/images/409.jpg"');
update archive_article set content = replace(content, '<img src="410"', '<img src="/site_media/media/files/archive/urbis/images/410.jpg"');
update archive_article set content = replace(content, '<img src="411"', '<img src="/site_media/media/files/archive/urbis/images/411.jpg"');
update archive_article set content = replace(content, '<img src="412"', '<img src="/site_media/media/files/archive/urbis/images/412.jpg"');
update archive_article set content = replace(content, '<img src="413"', '<img src="/site_media/media/files/archive/urbis/images/413.jpg"');
update archive_article set content = replace(content, '<img src="414"', '<img src="/site_media/media/files/archive/urbis/images/414.jpg"');
update archive_article set content = replace(content, '<img src="415"', '<img src="/site_media/media/files/archive/urbis/images/415.jpg"');
update archive_article set content = replace(content, '<img src="416"', '<img src="/site_media/media/files/archive/urbis/images/416.jpg"');
update archive_article set content = replace(content, '<img src="417"', '<img src="/site_media/media/files/archive/urbis/images/417.jpg"');
update archive_article set content = replace(content, '<img src="418"', '<img src="/site_media/media/files/archive/urbis/images/418.jpg"');
update archive_article set content = replace(content, '<img src="419"', '<img src="/site_media/media/files/archive/urbis/images/419.jpg"');
update archive_article set content = replace(content, '<img src="420"', '<img src="/site_media/media/files/archive/urbis/images/420.jpg"');
update archive_article set content = replace(content, '<img src="421"', '<img src="/site_media/media/files/archive/urbis/images/421.jpg"');
update archive_article set content = replace(content, '<img src="422"', '<img src="/site_media/media/files/archive/urbis/images/422.jpg"');
update archive_article set content = replace(content, '<img src="423"', '<img src="/site_media/media/files/archive/urbis/images/423.jpg"');
update archive_article set content = replace(content, '<img src="424"', '<img src="/site_media/media/files/archive/urbis/images/424.jpg"');
update archive_article set content = replace(content, '<img src="425"', '<img src="/site_media/media/files/archive/urbis/images/425.jpg"');
update archive_article set content = replace(content, '<img src="426"', '<img src="/site_media/media/files/archive/urbis/images/426.jpg"');
update archive_article set content = replace(content, '<img src="427"', '<img src="/site_media/media/files/archive/urbis/images/427.jpg"');
update archive_article set content = replace(content, '<img src="428"', '<img src="/site_media/media/files/archive/urbis/images/428.jpg"');
update archive_article set content = replace(content, '<img src="429"', '<img src="/site_media/media/files/archive/urbis/images/429.jpg"');
update archive_article set content = replace(content, '<img src="430"', '<img src="/site_media/media/files/archive/urbis/images/430.jpg"');
update archive_article set content = replace(content, '<img src="431"', '<img src="/site_media/media/files/archive/urbis/images/431.jpg"');
update archive_article set content = replace(content, '<img src="432"', '<img src="/site_media/media/files/archive/urbis/images/432.jpg"');
update archive_article set content = replace(content, '<img src="433"', '<img src="/site_media/media/files/archive/urbis/images/433.jpg"');
update archive_article set content = replace(content, '<img src="439"', '<img src="/site_media/media/files/archive/urbis/images/439.jpg"');
update archive_article set content = replace(content, '<img src="435"', '<img src="/site_media/media/files/archive/urbis/images/435.jpg"');
update archive_article set content = replace(content, '<img src="436"', '<img src="/site_media/media/files/archive/urbis/images/436.jpg"');
update archive_article set content = replace(content, '<img src="437"', '<img src="/site_media/media/files/archive/urbis/images/437.jpg"');
update archive_article set content = replace(content, '<img src="438"', '<img src="/site_media/media/files/archive/urbis/images/438.jpg"');
update archive_article set content = replace(content, '<img src="440"', '<img src="/site_media/media/files/archive/urbis/images/440.jpg"');
update archive_article set content = replace(content, '<img src="441"', '<img src="/site_media/media/files/archive/urbis/images/441.jpg"');
update archive_article set content = replace(content, '<img src="442"', '<img src="/site_media/media/files/archive/urbis/images/442.jpg"');
update archive_article set content = replace(content, '<img src="443"', '<img src="/site_media/media/files/archive/urbis/images/443.jpg"');
update archive_article set content = replace(content, '<img src="444"', '<img src="/site_media/media/files/archive/urbis/images/444.jpg"');
update archive_article set content = replace(content, '<img src="445"', '<img src="/site_media/media/files/archive/urbis/images/445.jpg"');
update archive_article set content = replace(content, '<img src="446"', '<img src="/site_media/media/files/archive/urbis/images/446.jpg"');
update archive_article set content = replace(content, '<img src="447"', '<img src="/site_media/media/files/archive/urbis/images/447.jpg"');
update archive_article set content = replace(content, '<img src="448"', '<img src="/site_media/media/files/archive/urbis/images/448.jpg"');
update archive_article set content = replace(content, '<img src="449"', '<img src="/site_media/media/files/archive/urbis/images/449.jpg"');
update archive_article set content = replace(content, '<img src="450"', '<img src="/site_media/media/files/archive/urbis/images/450.jpg"');
update archive_article set content = replace(content, '<img src="451"', '<img src="/site_media/media/files/archive/urbis/images/451.jpg"');
update archive_article set content = replace(content, '<img src="452"', '<img src="/site_media/media/files/archive/urbis/images/452.jpg"');
update archive_article set content = replace(content, '<img src="453"', '<img src="/site_media/media/files/archive/urbis/images/453.jpg"');
update archive_article set content = replace(content, '<img src="454"', '<img src="/site_media/media/files/archive/urbis/images/454.jpg"');
update archive_article set content = replace(content, '<img src="455"', '<img src="/site_media/media/files/archive/urbis/images/455.jpg"');
update archive_article set content = replace(content, '<img src="456"', '<img src="/site_media/media/files/archive/urbis/images/456.jpg"');
update archive_article set content = replace(content, '<img src="457"', '<img src="/site_media/media/files/archive/urbis/images/457.jpg"');
update archive_article set content = replace(content, '<img src="458"', '<img src="/site_media/media/files/archive/urbis/images/458.jpg"');
update archive_article set content = replace(content, '<img src="459"', '<img src="/site_media/media/files/archive/urbis/images/459.jpg"');
update archive_article set content = replace(content, '<img src="460"', '<img src="/site_media/media/files/archive/urbis/images/460.png"');
update archive_article set content = replace(content, '<img src="461"', '<img src="/site_media/media/files/archive/urbis/images/461.jpg"');
update archive_article set content = replace(content, '<img src="462"', '<img src="/site_media/media/files/archive/urbis/images/462.jpg"');
update archive_article set content = replace(content, '<img src="463"', '<img src="/site_media/media/files/archive/urbis/images/463.jpg"');
update archive_article set content = replace(content, '<img src="464"', '<img src="/site_media/media/files/archive/urbis/images/464.jpg"');
update archive_article set content = replace(content, '<img src="465"', '<img src="/site_media/media/files/archive/urbis/images/465.jpg"');
update archive_article set content = replace(content, '<img src="466"', '<img src="/site_media/media/files/archive/urbis/images/466.jpg"');
update archive_article set content = replace(content, '<img src="467"', '<img src="/site_media/media/files/archive/urbis/images/467.jpg"');
update archive_article set content = replace(content, '<img src="468"', '<img src="/site_media/media/files/archive/urbis/images/468.jpg"');
update archive_article set content = replace(content, '<img src="469"', '<img src="/site_media/media/files/archive/urbis/images/469.jpg"');
update archive_article set content = replace(content, '<img src="470"', '<img src="/site_media/media/files/archive/urbis/images/470.jpg"');
update archive_article set content = replace(content, '<img src="471"', '<img src="/site_media/media/files/archive/urbis/images/471.jpg"');
update archive_article set content = replace(content, '<img src="472"', '<img src="/site_media/media/files/archive/urbis/images/472.jpg"');
update archive_article set content = replace(content, '<img src="473"', '<img src="/site_media/media/files/archive/urbis/images/473.jpg"');
update archive_article set content = replace(content, '<img src="474"', '<img src="/site_media/media/files/archive/urbis/images/474.jpg"');
update archive_article set content = replace(content, '<img src="475"', '<img src="/site_media/media/files/archive/urbis/images/475.jpg"');
update archive_article set content = replace(content, '<img src="476"', '<img src="/site_media/media/files/archive/urbis/images/476.jpg"');
update archive_article set content = replace(content, '<img src="477"', '<img src="/site_media/media/files/archive/urbis/images/477.jpg"');
update archive_article set content = replace(content, '<img src="478"', '<img src="/site_media/media/files/archive/urbis/images/478.jpg"');
update archive_article set content = replace(content, '<img src="479"', '<img src="/site_media/media/files/archive/urbis/images/479.jpg"');
update archive_article set content = replace(content, '<img src="480"', '<img src="/site_media/media/files/archive/urbis/images/480.jpg"');
update archive_article set content = replace(content, '<img src="486"', '<img src="/site_media/media/files/archive/urbis/images/486.jpg"');
update archive_article set content = replace(content, '<img src="482"', '<img src="/site_media/media/files/archive/urbis/images/482.jpg"');
update archive_article set content = replace(content, '<img src="483"', '<img src="/site_media/media/files/archive/urbis/images/483.jpg"');
update archive_article set content = replace(content, '<img src="485"', '<img src="/site_media/media/files/archive/urbis/images/485.jpg"');
update archive_article set content = replace(content, '<img src="495"', '<img src="/site_media/media/files/archive/urbis/images/495.jpg"');
update archive_article set content = replace(content, '<img src="494"', '<img src="/site_media/media/files/archive/urbis/images/494.jpg"');
update archive_article set content = replace(content, '<img src="488"', '<img src="/site_media/media/files/archive/urbis/images/488.jpg"');
update archive_article set content = replace(content, '<img src="493"', '<img src="/site_media/media/files/archive/urbis/images/493.jpg"');
update archive_article set content = replace(content, '<img src="496"', '<img src="/site_media/media/files/archive/urbis/images/496.jpg"');
update archive_article set content = replace(content, '<img src="497"', '<img src="/site_media/media/files/archive/urbis/images/497.jpg"');
update archive_article set content = replace(content, '<img src="498"', '<img src="/site_media/media/files/archive/urbis/images/498.jpg"');
update archive_article set content = replace(content, '<img src="499"', '<img src="/site_media/media/files/archive/urbis/images/499.jpg"');
update archive_article set content = replace(content, '<img src="500"', '<img src="/site_media/media/files/archive/urbis/images/500.jpg"');
update archive_article set content = replace(content, '<img src="501"', '<img src="/site_media/media/files/archive/urbis/images/501.jpg"');
update archive_article set content = replace(content, '<img src="502"', '<img src="/site_media/media/files/archive/urbis/images/502.jpg"');
update archive_article set content = replace(content, '<img src="503"', '<img src="/site_media/media/files/archive/urbis/images/503.jpg"');
update archive_article set content = replace(content, '<img src="504"', '<img src="/site_media/media/files/archive/urbis/images/504.jpg"');
update archive_article set content = replace(content, '<img src="505"', '<img src="/site_media/media/files/archive/urbis/images/505.jpg"');
update archive_article set content = replace(content, '<img src="506"', '<img src="/site_media/media/files/archive/urbis/images/506.jpg"');
update archive_article set content = replace(content, '<img src="507"', '<img src="/site_media/media/files/archive/urbis/images/507.jpg"');
update archive_article set content = replace(content, '<img src="508"', '<img src="/site_media/media/files/archive/urbis/images/508.jpg"');
update archive_article set content = replace(content, '<img src="509"', '<img src="/site_media/media/files/archive/urbis/images/509.jpg"');
update archive_article set content = replace(content, '<img src="510"', '<img src="/site_media/media/files/archive/urbis/images/510.jpg"');
update archive_article set content = replace(content, '<img src="511"', '<img src="/site_media/media/files/archive/urbis/images/511.jpg"');
update archive_article set content = replace(content, '<img src="512"', '<img src="/site_media/media/files/archive/urbis/images/512.jpg"');
update archive_article set content = replace(content, '<img src="513"', '<img src="/site_media/media/files/archive/urbis/images/513.jpg"');
update archive_article set content = replace(content, '<img src="514"', '<img src="/site_media/media/files/archive/urbis/images/514.jpg"');
update archive_article set content = replace(content, '<img src="515"', '<img src="/site_media/media/files/archive/urbis/images/515.jpg"');
update archive_article set content = replace(content, '<img src="516"', '<img src="/site_media/media/files/archive/urbis/images/516.jpg"');
update archive_article set content = replace(content, '<img src="517"', '<img src="/site_media/media/files/archive/urbis/images/517.jpg"');
update archive_article set content = replace(content, '<img src="518"', '<img src="/site_media/media/files/archive/urbis/images/518.jpg"');
update archive_article set content = replace(content, '<img src="535"', '<img src="/site_media/media/files/archive/urbis/images/535.jpg"');
update archive_article set content = replace(content, '<img src="528"', '<img src="/site_media/media/files/archive/urbis/images/528.jpg"');
update archive_article set content = replace(content, '<img src="527"', '<img src="/site_media/media/files/archive/urbis/images/527.jpg"');
update archive_article set content = replace(content, '<img src="530"', '<img src="/site_media/media/files/archive/urbis/images/530.jpg"');
update archive_article set content = replace(content, '<img src="529"', '<img src="/site_media/media/files/archive/urbis/images/529.jpg"');
update archive_article set content = replace(content, '<img src="532"', '<img src="/site_media/media/files/archive/urbis/images/532.jpg"');
update archive_article set content = replace(content, '<img src="531"', '<img src="/site_media/media/files/archive/urbis/images/531.jpg"');
update archive_article set content = replace(content, '<img src="534"', '<img src="/site_media/media/files/archive/urbis/images/534.jpg"');
update archive_article set content = replace(content, '<img src="533"', '<img src="/site_media/media/files/archive/urbis/images/533.jpg"');
update archive_article set content = replace(content, '<img src="536"', '<img src="/site_media/media/files/archive/urbis/images/536.jpg"');
update archive_article set content = replace(content, '<img src="537"', '<img src="/site_media/media/files/archive/urbis/images/537.jpg"');
update archive_article set content = replace(content, '<img src="538"', '<img src="/site_media/media/files/archive/urbis/images/538.jpg"');
update archive_article set content = replace(content, '<img src="539"', '<img src="/site_media/media/files/archive/urbis/images/539.jpg"');
update archive_article set content = replace(content, '<img src="540"', '<img src="/site_media/media/files/archive/urbis/images/540.jpg"');
update archive_article set content = replace(content, '<img src="541"', '<img src="/site_media/media/files/archive/urbis/images/541.jpg"');
update archive_article set content = replace(content, '<img src="542"', '<img src="/site_media/media/files/archive/urbis/images/542.jpg"');
update archive_article set content = replace(content, '<img src="543"', '<img src="/site_media/media/files/archive/urbis/images/543.jpg"');
update archive_article set content = replace(content, '<img src="544"', '<img src="/site_media/media/files/archive/urbis/images/544.jpg"');
update archive_article set content = replace(content, '<img src="545"', '<img src="/site_media/media/files/archive/urbis/images/545.jpg"');
update archive_article set content = replace(content, '<img src="546"', '<img src="/site_media/media/files/archive/urbis/images/546.jpg"');
update archive_article set content = replace(content, '<img src="547"', '<img src="/site_media/media/files/archive/urbis/images/547.jpg"');
update archive_article set content = replace(content, '<img src="548"', '<img src="/site_media/media/files/archive/urbis/images/548.jpg"');
update archive_article set content = replace(content, '<img src="549"', '<img src="/site_media/media/files/archive/urbis/images/549.jpg"');
update archive_article set content = replace(content, '<img src="552"', '<img src="/site_media/media/files/archive/urbis/images/552.jpg"');
update archive_article set content = replace(content, '<img src="551"', '<img src="/site_media/media/files/archive/urbis/images/551.jpg"');
update archive_article set content = replace(content, '<img src="553"', '<img src="/site_media/media/files/archive/urbis/images/553.jpg"');
update archive_article set content = replace(content, '<img src="554"', '<img src="/site_media/media/files/archive/urbis/images/554.jpg"');
update archive_article set content = replace(content, '<img src="555"', '<img src="/site_media/media/files/archive/urbis/images/555.jpg"');
update archive_article set content = replace(content, '<img src="556"', '<img src="/site_media/media/files/archive/urbis/images/556.jpg"');
update archive_article set content = replace(content, '<img src="557"', '<img src="/site_media/media/files/archive/urbis/images/557.jpg"');
update archive_article set content = replace(content, '<img src="558"', '<img src="/site_media/media/files/archive/urbis/images/558.jpg"');
update archive_article set content = replace(content, '<img src="559"', '<img src="/site_media/media/files/archive/urbis/images/559.jpg"');
update archive_article set content = replace(content, '<img src="560"', '<img src="/site_media/media/files/archive/urbis/images/560.jpg"');
update archive_article set content = replace(content, '<img src="561"', '<img src="/site_media/media/files/archive/urbis/images/561.jpg"');
update archive_article set content = replace(content, '<img src="563"', '<img src="/site_media/media/files/archive/urbis/images/563.jpg"');
update archive_article set content = replace(content, '<img src="564"', '<img src="/site_media/media/files/archive/urbis/images/564.jpg"');
update archive_article set content = replace(content, '<img src="565"', '<img src="/site_media/media/files/archive/urbis/images/565.jpg"');
update archive_article set content = replace(content, '<img src="566"', '<img src="/site_media/media/files/archive/urbis/images/566.jpg"');
update archive_article set content = replace(content, '<img src="567"', '<img src="/site_media/media/files/archive/urbis/images/567.jpg"');
update archive_article set content = replace(content, '<img src="568"', '<img src="/site_media/media/files/archive/urbis/images/568.jpg"');
update archive_article set content = replace(content, '<img src="569"', '<img src="/site_media/media/files/archive/urbis/images/569.jpg"');
update archive_article set content = replace(content, '<img src="570"', '<img src="/site_media/media/files/archive/urbis/images/570.jpg"');
update archive_article set content = replace(content, '<img src="571"', '<img src="/site_media/media/files/archive/urbis/images/571.jpg"');
update archive_article set content = replace(content, '<img src="572"', '<img src="/site_media/media/files/archive/urbis/images/572.jpg"');
update archive_article set content = replace(content, '<img src="573"', '<img src="/site_media/media/files/archive/urbis/images/573.jpg"');
update archive_article set content = replace(content, '<img src="574"', '<img src="/site_media/media/files/archive/urbis/images/574.jpg"');
update archive_article set content = replace(content, '<img src="575"', '<img src="/site_media/media/files/archive/urbis/images/575.jpg"');
update archive_article set content = replace(content, '<img src="576"', '<img src="/site_media/media/files/archive/urbis/images/576.jpg"');
update archive_article set content = replace(content, '<img src="577"', '<img src="/site_media/media/files/archive/urbis/images/577.jpg"');
update archive_article set content = replace(content, '<img src="578"', '<img src="/site_media/media/files/archive/urbis/images/578.jpg"');
update archive_article set content = replace(content, '<img src="579"', '<img src="/site_media/media/files/archive/urbis/images/579.jpg"');
update archive_article set content = replace(content, '<img src="580"', '<img src="/site_media/media/files/archive/urbis/images/580.jpg"');
update archive_article set content = replace(content, '<img src="581"', '<img src="/site_media/media/files/archive/urbis/images/581.jpg"');
update archive_article set content = replace(content, '<img src="582"', '<img src="/site_media/media/files/archive/urbis/images/582.jpg"');
update archive_article set content = replace(content, '<img src="583"', '<img src="/site_media/media/files/archive/urbis/images/583.jpg"');
update archive_article set content = replace(content, '<img src="584"', '<img src="/site_media/media/files/archive/urbis/images/584.jpg"');
update archive_article set content = replace(content, '<img src="585"', '<img src="/site_media/media/files/archive/urbis/images/585.jpg"');
update archive_article set content = replace(content, '<img src="586"', '<img src="/site_media/media/files/archive/urbis/images/586.jpg"');
update archive_article set content = replace(content, '<img src="587"', '<img src="/site_media/media/files/archive/urbis/images/587.jpg"');
update archive_article set content = replace(content, '<img src="588"', '<img src="/site_media/media/files/archive/urbis/images/588.jpg"');
update archive_article set content = replace(content, '<img src="589"', '<img src="/site_media/media/files/archive/urbis/images/589.jpg"');
update archive_article set content = replace(content, '<img src="590"', '<img src="/site_media/media/files/archive/urbis/images/590.jpg"');
update archive_article set content = replace(content, '<img src="591"', '<img src="/site_media/media/files/archive/urbis/images/591.jpg"');
update archive_article set content = replace(content, '<img src="592"', '<img src="/site_media/media/files/archive/urbis/images/592.jpg"');
update archive_article set content = replace(content, '<img src="593"', '<img src="/site_media/media/files/archive/urbis/images/593.jpg"');
update archive_article set content = replace(content, '<img src="594"', '<img src="/site_media/media/files/archive/urbis/images/594.jpg"');
update archive_article set content = replace(content, '<img src="595"', '<img src="/site_media/media/files/archive/urbis/images/595.jpg"');
update archive_article set content = replace(content, '<img src="596"', '<img src="/site_media/media/files/archive/urbis/images/596.jpg"');
update archive_article set content = replace(content, '<img src="597"', '<img src="/site_media/media/files/archive/urbis/images/597.jpg"');
update archive_article set content = replace(content, '<img src="598"', '<img src="/site_media/media/files/archive/urbis/images/598.jpg"');
update archive_article set content = replace(content, '<img src="599"', '<img src="/site_media/media/files/archive/urbis/images/599.jpg"');
update archive_article set content = replace(content, '<img src="600"', '<img src="/site_media/media/files/archive/urbis/images/600.jpg"');
update archive_article set content = replace(content, '<img src="601"', '<img src="/site_media/media/files/archive/urbis/images/601.jpg"');
update archive_article set content = replace(content, '<img src="602"', '<img src="/site_media/media/files/archive/urbis/images/602.jpg"');
update archive_article set content = replace(content, '<img src="606"', '<img src="/site_media/media/files/archive/urbis/images/606.jpg"');
update archive_article set content = replace(content, '<img src="605"', '<img src="/site_media/media/files/archive/urbis/images/605.jpg"');
update archive_article set content = replace(content, '<img src="607"', '<img src="/site_media/media/files/archive/urbis/images/607.jpg"');
update archive_article set content = replace(content, '<img src="608"', '<img src="/site_media/media/files/archive/urbis/images/608.jpg"');
update archive_article set content = replace(content, '<img src="609"', '<img src="/site_media/media/files/archive/urbis/images/609.jpg"');
update archive_article set content = replace(content, '<img src="610"', '<img src="/site_media/media/files/archive/urbis/images/610.jpg"');
update archive_article set content = replace(content, '<img src="611"', '<img src="/site_media/media/files/archive/urbis/images/611.jpg"');
update archive_article set content = replace(content, '<img src="612"', '<img src="/site_media/media/files/archive/urbis/images/612.jpg"');
update archive_article set content = replace(content, '<img src="613"', '<img src="/site_media/media/files/archive/urbis/images/613.jpg"');
update archive_article set content = replace(content, '<img src="614"', '<img src="/site_media/media/files/archive/urbis/images/614.jpg"');
update archive_article set content = replace(content, '<img src="615"', '<img src="/site_media/media/files/archive/urbis/images/615.jpg"');
update archive_article set content = replace(content, '<img src="616"', '<img src="/site_media/media/files/archive/urbis/images/616.jpg"');
update archive_article set content = replace(content, '<img src="617"', '<img src="/site_media/media/files/archive/urbis/images/617.jpg"');
update archive_article set content = replace(content, '<img src="618"', '<img src="/site_media/media/files/archive/urbis/images/618.jpg"');
update archive_article set content = replace(content, '<img src="619"', '<img src="/site_media/media/files/archive/urbis/images/619.jpg"');
update archive_article set content = replace(content, '<img src="620"', '<img src="/site_media/media/files/archive/urbis/images/620.jpg"');
update archive_article set content = replace(content, '<img src="621"', '<img src="/site_media/media/files/archive/urbis/images/621.jpg"');
update archive_article set content = replace(content, '<img src="624"', '<img src="/site_media/media/files/archive/urbis/images/624.jpg"');
update archive_article set content = replace(content, '<img src="623"', '<img src="/site_media/media/files/archive/urbis/images/623.jpg"');
update archive_article set content = replace(content, '<img src="627"', '<img src="/site_media/media/files/archive/urbis/images/627.jpg"');
update archive_article set content = replace(content, '<img src="626"', '<img src="/site_media/media/files/archive/urbis/images/626.jpg"');
update archive_article set content = replace(content, '<img src="628"', '<img src="/site_media/media/files/archive/urbis/images/628.jpg"');
update archive_article set content = replace(content, '<img src="629"', '<img src="/site_media/media/files/archive/urbis/images/629.jpg"');
update archive_article set content = replace(content, '<img src="630"', '<img src="/site_media/media/files/archive/urbis/images/630.jpg"');
update archive_article set content = replace(content, '<img src="631"', '<img src="/site_media/media/files/archive/urbis/images/631.jpg"');
update archive_article set content = replace(content, '<img src="632"', '<img src="/site_media/media/files/archive/urbis/images/632.jpg"');
update archive_article set content = replace(content, '<img src="633"', '<img src="/site_media/media/files/archive/urbis/images/633.jpg"');
update archive_article set content = replace(content, '<img src="634"', '<img src="/site_media/media/files/archive/urbis/images/634.jpg"');
update archive_article set content = replace(content, '<img src="635"', '<img src="/site_media/media/files/archive/urbis/images/635.jpg"');
update archive_article set content = replace(content, '<img src="636"', '<img src="/site_media/media/files/archive/urbis/images/636.jpg"');
update archive_article set content = replace(content, '<img src="639"', '<img src="/site_media/media/files/archive/urbis/images/639.jpg"');
update archive_article set content = replace(content, '<img src="638"', '<img src="/site_media/media/files/archive/urbis/images/638.jpg"');
update archive_article set content = replace(content, '<img src="640"', '<img src="/site_media/media/files/archive/urbis/images/640.jpg"');
update archive_article set content = replace(content, '<img src="641"', '<img src="/site_media/media/files/archive/urbis/images/641.jpg"');
update archive_article set content = replace(content, '<img src="642"', '<img src="/site_media/media/files/archive/urbis/images/642.jpg"');
update archive_article set content = replace(content, '<img src="643"', '<img src="/site_media/media/files/archive/urbis/images/643.jpg"');
update archive_article set content = replace(content, '<img src="644"', '<img src="/site_media/media/files/archive/urbis/images/644.jpg"');
update archive_article set content = replace(content, '<img src="645"', '<img src="/site_media/media/files/archive/urbis/images/645.jpg"');
update archive_article set content = replace(content, '<img src="646"', '<img src="/site_media/media/files/archive/urbis/images/646.jpg"');
update archive_article set content = replace(content, '<img src="647"', '<img src="/site_media/media/files/archive/urbis/images/647.jpg"');
update archive_article set content = replace(content, '<img src="648"', '<img src="/site_media/media/files/archive/urbis/images/648.jpg"');
update archive_article set content = replace(content, '<img src="649"', '<img src="/site_media/media/files/archive/urbis/images/649.jpg"');
update archive_article set content = replace(content, '<img src="650"', '<img src="/site_media/media/files/archive/urbis/images/650.jpg"');
update archive_article set content = replace(content, '<img src="651"', '<img src="/site_media/media/files/archive/urbis/images/651.jpg"');
update archive_article set content = replace(content, '<img src="652"', '<img src="/site_media/media/files/archive/urbis/images/652.jpg"');
update archive_article set content = replace(content, '<img src="653"', '<img src="/site_media/media/files/archive/urbis/images/653.jpg"');
update archive_article set content = replace(content, '<img src="654"', '<img src="/site_media/media/files/archive/urbis/images/654.jpg"');
update archive_article set content = replace(content, '<img src="655"', '<img src="/site_media/media/files/archive/urbis/images/655.jpg"');
update archive_article set content = replace(content, '<img src="656"', '<img src="/site_media/media/files/archive/urbis/images/656.jpg"');
update archive_article set content = replace(content, '<img src="657"', '<img src="/site_media/media/files/archive/urbis/images/657.jpg"');
update archive_article set content = replace(content, '<img src="658"', '<img src="/site_media/media/files/archive/urbis/images/658.jpg"');
update archive_article set content = replace(content, '<img src="659"', '<img src="/site_media/media/files/archive/urbis/images/659.jpg"');
update archive_article set content = replace(content, '<img src="660"', '<img src="/site_media/media/files/archive/urbis/images/660.jpg"');
update archive_article set content = replace(content, '<img src="661"', '<img src="/site_media/media/files/archive/urbis/images/661.jpg"');
update archive_article set content = replace(content, '<img src="662"', '<img src="/site_media/media/files/archive/urbis/images/662.jpg"');
update archive_article set content = replace(content, '<img src="663"', '<img src="/site_media/media/files/archive/urbis/images/663.jpg"');
update archive_article set content = replace(content, '<img src="664"', '<img src="/site_media/media/files/archive/urbis/images/664.jpg"');
update archive_article set content = replace(content, '<img src="665"', '<img src="/site_media/media/files/archive/urbis/images/665.jpg"');
update archive_article set content = replace(content, '<img src="666"', '<img src="/site_media/media/files/archive/urbis/images/666.jpg"');
update archive_article set content = replace(content, '<img src="669"', '<img src="/site_media/media/files/archive/urbis/images/669.jpg"');
update archive_article set content = replace(content, '<img src="668"', '<img src="/site_media/media/files/archive/urbis/images/668.jpg"');
update archive_article set content = replace(content, '<img src="670"', '<img src="/site_media/media/files/archive/urbis/images/670.jpg"');
update archive_article set content = replace(content, '<img src="671"', '<img src="/site_media/media/files/archive/urbis/images/671.jpg"');
update archive_article set content = replace(content, '<img src="672"', '<img src="/site_media/media/files/archive/urbis/images/672.jpg"');
update archive_article set content = replace(content, '<img src="673"', '<img src="/site_media/media/files/archive/urbis/images/673.jpg"');
update archive_article set content = replace(content, '<img src="674"', '<img src="/site_media/media/files/archive/urbis/images/674.jpg"');
update archive_article set content = replace(content, '<img src="675"', '<img src="/site_media/media/files/archive/urbis/images/675.jpg"');
update archive_article set content = replace(content, '<img src="680"', '<img src="/site_media/media/files/archive/urbis/images/680.jpg"');
update archive_article set content = replace(content, '<img src="677"', '<img src="/site_media/media/files/archive/urbis/images/677.jpg"');
update archive_article set content = replace(content, '<img src="678"', '<img src="/site_media/media/files/archive/urbis/images/678.jpg"');
update archive_article set content = replace(content, '<img src="679"', '<img src="/site_media/media/files/archive/urbis/images/679.jpg"');
update archive_article set content = replace(content, '<img src="681"', '<img src="/site_media/media/files/archive/urbis/images/681.jpg"');
update archive_article set content = replace(content, '<img src="682"', '<img src="/site_media/media/files/archive/urbis/images/682.jpg"');
update archive_article set content = replace(content, '<img src="683"', '<img src="/site_media/media/files/archive/urbis/images/683.jpg"');
update archive_article set content = replace(content, '<img src="684"', '<img src="/site_media/media/files/archive/urbis/images/684.jpg"');
update archive_article set content = replace(content, '<img src="685"', '<img src="/site_media/media/files/archive/urbis/images/685.jpg"');
update archive_article set content = replace(content, '<img src="686"', '<img src="/site_media/media/files/archive/urbis/images/686.jpg"');
update archive_article set content = replace(content, '<img src="687"', '<img src="/site_media/media/files/archive/urbis/images/687.jpg"');
update archive_article set content = replace(content, '<img src="688"', '<img src="/site_media/media/files/archive/urbis/images/688.jpg"');
update archive_article set content = replace(content, '<img src="689"', '<img src="/site_media/media/files/archive/urbis/images/689.jpg"');
update archive_article set content = replace(content, '<img src="690"', '<img src="/site_media/media/files/archive/urbis/images/690.jpg"');
update archive_article set content = replace(content, '<img src="691"', '<img src="/site_media/media/files/archive/urbis/images/691.jpg"');
update archive_article set content = replace(content, '<img src="692"', '<img src="/site_media/media/files/archive/urbis/images/692.jpg"');
update archive_article set content = replace(content, '<img src="693"', '<img src="/site_media/media/files/archive/urbis/images/693.jpg"');
update archive_article set content = replace(content, '<img src="694"', '<img src="/site_media/media/files/archive/urbis/images/694.jpg"');
update archive_article set content = replace(content, '<img src="695"', '<img src="/site_media/media/files/archive/urbis/images/695.jpg"');
update archive_article set content = replace(content, '<img src="696"', '<img src="/site_media/media/files/archive/urbis/images/696.jpg"');
update archive_article set content = replace(content, '<img src="697"', '<img src="/site_media/media/files/archive/urbis/images/697.jpg"');
update archive_article set content = replace(content, '<img src="698"', '<img src="/site_media/media/files/archive/urbis/images/698.jpg"');
update archive_article set content = replace(content, '<img src="699"', '<img src="/site_media/media/files/archive/urbis/images/699.jpg"');
update archive_article set content = replace(content, '<img src="700"', '<img src="/site_media/media/files/archive/urbis/images/700.jpg"');
update archive_article set content = replace(content, '<img src="701"', '<img src="/site_media/media/files/archive/urbis/images/701.jpg"');
update archive_article set content = replace(content, '<img src="702"', '<img src="/site_media/media/files/archive/urbis/images/702.jpg"');
update archive_article set content = replace(content, '<img src="703"', '<img src="/site_media/media/files/archive/urbis/images/703.jpg"');
update archive_article set content = replace(content, '<img src="704"', '<img src="/site_media/media/files/archive/urbis/images/704.jpg"');
update archive_article set content = replace(content, '<img src="705"', '<img src="/site_media/media/files/archive/urbis/images/705.jpg"');
update archive_article set content = replace(content, '<img src="706"', '<img src="/site_media/media/files/archive/urbis/images/706.jpg"');
update archive_article set content = replace(content, '<img src="707"', '<img src="/site_media/media/files/archive/urbis/images/707.jpg"');
update archive_article set content = replace(content, '<img src="708"', '<img src="/site_media/media/files/archive/urbis/images/708.jpg"');
update archive_article set content = replace(content, '<img src="709"', '<img src="/site_media/media/files/archive/urbis/images/709.jpg"');
update archive_article set content = replace(content, '<img src="710"', '<img src="/site_media/media/files/archive/urbis/images/710.jpg"');
update archive_article set content = replace(content, '<img src="711"', '<img src="/site_media/media/files/archive/urbis/images/711.jpg"');
update archive_article set content = replace(content, '<img src="712"', '<img src="/site_media/media/files/archive/urbis/images/712.jpg"');
update archive_article set content = replace(content, '<img src="713"', '<img src="/site_media/media/files/archive/urbis/images/713.jpg"');
update archive_article set content = replace(content, '<img src="714"', '<img src="/site_media/media/files/archive/urbis/images/714.jpg"');
update archive_article set content = replace(content, '<img src="715"', '<img src="/site_media/media/files/archive/urbis/images/715.jpg"');
update archive_article set content = replace(content, '<img src="716"', '<img src="/site_media/media/files/archive/urbis/images/716.jpg"');
update archive_article set content = replace(content, '<img src="717"', '<img src="/site_media/media/files/archive/urbis/images/717.jpg"');
update archive_article set content = replace(content, '<img src="718"', '<img src="/site_media/media/files/archive/urbis/images/718.jpg"');
update archive_article set content = replace(content, '<img src="719"', '<img src="/site_media/media/files/archive/urbis/images/719.jpg"');
update archive_article set content = replace(content, '<img src="720"', '<img src="/site_media/media/files/archive/urbis/images/720.jpg"');
update archive_article set content = replace(content, '<img src="721"', '<img src="/site_media/media/files/archive/urbis/images/721.jpg"');
update archive_article set content = replace(content, '<img src="722"', '<img src="/site_media/media/files/archive/urbis/images/722.jpg"');
update archive_article set content = replace(content, '<img src="723"', '<img src="/site_media/media/files/archive/urbis/images/723.jpg"');
update archive_article set content = replace(content, '<img src="724"', '<img src="/site_media/media/files/archive/urbis/images/724.jpg"');
update archive_article set content = replace(content, '<img src="725"', '<img src="/site_media/media/files/archive/urbis/images/725.jpg"');
update archive_article set content = replace(content, '<img src="726"', '<img src="/site_media/media/files/archive/urbis/images/726.jpg"');
update archive_article set content = replace(content, '<img src="727"', '<img src="/site_media/media/files/archive/urbis/images/727.jpg"');
update archive_article set content = replace(content, '<img src="728"', '<img src="/site_media/media/files/archive/urbis/images/728.jpg"');
update archive_article set content = replace(content, '<img src="729"', '<img src="/site_media/media/files/archive/urbis/images/729.jpg"');
update archive_article set content = replace(content, '<img src="730"', '<img src="/site_media/media/files/archive/urbis/images/730.jpg"');
update archive_article set content = replace(content, '<img src="731"', '<img src="/site_media/media/files/archive/urbis/images/731.jpg"');
update archive_article set content = replace(content, '<img src="732"', '<img src="/site_media/media/files/archive/urbis/images/732.jpg"');
update archive_article set content = replace(content, '<img src="733"', '<img src="/site_media/media/files/archive/urbis/images/733.jpg"');
update archive_article set content = replace(content, '<img src="734"', '<img src="/site_media/media/files/archive/urbis/images/734.jpg"');
update archive_article set content = replace(content, '<img src="735"', '<img src="/site_media/media/files/archive/urbis/images/735.jpg"');
update archive_article set content = replace(content, '<img src="736"', '<img src="/site_media/media/files/archive/urbis/images/736.jpg"');
update archive_article set content = replace(content, '<img src="737"', '<img src="/site_media/media/files/archive/urbis/images/737.jpg"');
update archive_article set content = replace(content, '<img src="738"', '<img src="/site_media/media/files/archive/urbis/images/738.jpg"');
update archive_article set content = replace(content, '<img src="739"', '<img src="/site_media/media/files/archive/urbis/images/739.jpg"');
update archive_article set content = replace(content, '<img src="740"', '<img src="/site_media/media/files/archive/urbis/images/740.jpg"');
update archive_article set content = replace(content, '<img src="741"', '<img src="/site_media/media/files/archive/urbis/images/741.jpg"');
update archive_article set content = replace(content, '<img src="742"', '<img src="/site_media/media/files/archive/urbis/images/742.jpg"');
update archive_article set content = replace(content, '<img src="743"', '<img src="/site_media/media/files/archive/urbis/images/743.jpg"');
update archive_article set content = replace(content, '<img src="744"', '<img src="/site_media/media/files/archive/urbis/images/744.jpg"');
update archive_article set content = replace(content, '<img src="745"', '<img src="/site_media/media/files/archive/urbis/images/745.jpg"');
update archive_article set content = replace(content, '<img src="746"', '<img src="/site_media/media/files/archive/urbis/images/746.jpg"');
update archive_article set content = replace(content, '<img src="747"', '<img src="/site_media/media/files/archive/urbis/images/747.jpg"');
update archive_article set content = replace(content, '<img src="748"', '<img src="/site_media/media/files/archive/urbis/images/748.jpg"');
update archive_article set content = replace(content, '<img src="749"', '<img src="/site_media/media/files/archive/urbis/images/749.jpg"');
update archive_article set content = replace(content, '<img src="750"', '<img src="/site_media/media/files/archive/urbis/images/750.jpg"');
update archive_article set content = replace(content, '<img src="751"', '<img src="/site_media/media/files/archive/urbis/images/751.jpg"');
update archive_article set content = replace(content, '<img src="752"', '<img src="/site_media/media/files/archive/urbis/images/752.jpg"');
update archive_article set content = replace(content, '<img src="754"', '<img src="/site_media/media/files/archive/urbis/images/754.jpg"');
update archive_article set content = replace(content, '<img src="755"', '<img src="/site_media/media/files/archive/urbis/images/755.jpg"');
update archive_article set content = replace(content, '<img src="756"', '<img src="/site_media/media/files/archive/urbis/images/756.jpg"');
update archive_article set content = replace(content, '<img src="757"', '<img src="/site_media/media/files/archive/urbis/images/757.jpg"');
update archive_article set content = replace(content, '<img src="758"', '<img src="/site_media/media/files/archive/urbis/images/758.jpg"');
update archive_article set content = replace(content, '<img src="759"', '<img src="/site_media/media/files/archive/urbis/images/759.jpg"');
update archive_article set content = replace(content, '<img src="760"', '<img src="/site_media/media/files/archive/urbis/images/760.jpg"');
update archive_article set content = replace(content, '<img src="761"', '<img src="/site_media/media/files/archive/urbis/images/761.jpg"');
update archive_article set content = replace(content, '<img src="762"', '<img src="/site_media/media/files/archive/urbis/images/762.jpg"');
update archive_article set content = replace(content, '<img src="763"', '<img src="/site_media/media/files/archive/urbis/images/763.jpg"');
update archive_article set content = replace(content, '<img src="764"', '<img src="/site_media/media/files/archive/urbis/images/764.jpg"');
update archive_article set content = replace(content, '<img src="765"', '<img src="/site_media/media/files/archive/urbis/images/765.jpg"');
update archive_article set content = replace(content, '<img src="766"', '<img src="/site_media/media/files/archive/urbis/images/766.jpg"');
update archive_article set content = replace(content, '<img src="767"', '<img src="/site_media/media/files/archive/urbis/images/767.jpg"');
update archive_article set content = replace(content, '<img src="768"', '<img src="/site_media/media/files/archive/urbis/images/768.jpg"');
update archive_article set content = replace(content, '<img src="769"', '<img src="/site_media/media/files/archive/urbis/images/769.jpg"');
update archive_article set content = replace(content, '<img src="770"', '<img src="/site_media/media/files/archive/urbis/images/770.jpg"');
update archive_article set content = replace(content, '<img src="771"', '<img src="/site_media/media/files/archive/urbis/images/771.jpg"');
update archive_article set content = replace(content, '<img src="772"', '<img src="/site_media/media/files/archive/urbis/images/772.jpg"');
update archive_article set content = replace(content, '<img src="773"', '<img src="/site_media/media/files/archive/urbis/images/773.jpg"');
update archive_article set content = replace(content, '<img src="774"', '<img src="/site_media/media/files/archive/urbis/images/774.jpg"');
update archive_article set content = replace(content, '<img src="775"', '<img src="/site_media/media/files/archive/urbis/images/775.jpg"');
update archive_article set content = replace(content, '<img src="776"', '<img src="/site_media/media/files/archive/urbis/images/776.jpg"');
update archive_article set content = replace(content, '<img src="777"', '<img src="/site_media/media/files/archive/urbis/images/777.jpg"');
update archive_article set content = replace(content, '<img src="778"', '<img src="/site_media/media/files/archive/urbis/images/778.jpg"');
update archive_article set content = replace(content, '<img src="779"', '<img src="/site_media/media/files/archive/urbis/images/779.jpg"');
update archive_article set content = replace(content, '<img src="780"', '<img src="/site_media/media/files/archive/urbis/images/780.jpg"');
update archive_article set content = replace(content, '<img src="784"', '<img src="/site_media/media/files/archive/urbis/images/784.jpg"');
update archive_article set content = replace(content, '<img src="783"', '<img src="/site_media/media/files/archive/urbis/images/783.jpg"');
update archive_article set content = replace(content, '<img src="785"', '<img src="/site_media/media/files/archive/urbis/images/785.jpg"');
update archive_article set content = replace(content, '<img src="791"', '<img src="/site_media/media/files/archive/urbis/images/791.png"');
update archive_article set content = replace(content, '<img src="792"', '<img src="/site_media/media/files/archive/urbis/images/792.jpg"');
update archive_article set content = replace(content, '<img src="793"', '<img src="/site_media/media/files/archive/urbis/images/793.jpg"');
update archive_article set content = replace(content, '<img src="794"', '<img src="/site_media/media/files/archive/urbis/images/794.jpg"');
update archive_article set content = replace(content, '<img src="795"', '<img src="/site_media/media/files/archive/urbis/images/795.png"');
update archive_article set content = replace(content, '<img src="796"', '<img src="/site_media/media/files/archive/urbis/images/796.jpg"');
update archive_article set content = replace(content, '<img src="797"', '<img src="/site_media/media/files/archive/urbis/images/797.jpg"');
update archive_article set content = replace(content, '<img src="798"', '<img src="/site_media/media/files/archive/urbis/images/798.jpg"');
update archive_article set content = replace(content, '<img src="799"', '<img src="/site_media/media/files/archive/urbis/images/799.jpg"');
update archive_article set content = replace(content, '<img src="800"', '<img src="/site_media/media/files/archive/urbis/images/800.jpg"');
update archive_article set content = replace(content, '<img src="801"', '<img src="/site_media/media/files/archive/urbis/images/801.jpg"');
update archive_article set content = replace(content, '<img src="809"', '<img src="/site_media/media/files/archive/urbis/images/809.jpg"');
update archive_article set content = replace(content, '<img src="803"', '<img src="/site_media/media/files/archive/urbis/images/803.jpg"');
update archive_article set content = replace(content, '<img src="804"', '<img src="/site_media/media/files/archive/urbis/images/804.jpg"');
update archive_article set content = replace(content, '<img src="808"', '<img src="/site_media/media/files/archive/urbis/images/808.jpg"');
update archive_article set content = replace(content, '<img src="806"', '<img src="/site_media/media/files/archive/urbis/images/806.jpg"');
update archive_article set content = replace(content, '<img src="807"', '<img src="/site_media/media/files/archive/urbis/images/807.jpg"');
update archive_article set content = replace(content, '<img src="810"', '<img src="/site_media/media/files/archive/urbis/images/810.jpg"');
update archive_article set content = replace(content, '<img src="813"', '<img src="/site_media/media/files/archive/urbis/images/813.jpg"');
update archive_article set content = replace(content, '<img src="812"', '<img src="/site_media/media/files/archive/urbis/images/812.jpg"');
update archive_article set content = replace(content, '<img src="814"', '<img src="/site_media/media/files/archive/urbis/images/814.jpg"');
update archive_article set content = replace(content, '<img src="818"', '<img src="/site_media/media/files/archive/urbis/images/818.jpg"');
update archive_article set content = replace(content, '<img src="817"', '<img src="/site_media/media/files/archive/urbis/images/817.jpg"');
update archive_article set content = replace(content, '<img src="819"', '<img src="/site_media/media/files/archive/urbis/images/819.jpg"');
update archive_article set content = replace(content, '<img src="820"', '<img src="/site_media/media/files/archive/urbis/images/820.jpg"');
update archive_article set content = replace(content, '<img src="821"', '<img src="/site_media/media/files/archive/urbis/images/821.jpg"');
update archive_article set content = replace(content, '<img src="822"', '<img src="/site_media/media/files/archive/urbis/images/822.jpg"');
update archive_article set content = replace(content, '<img src="823"', '<img src="/site_media/media/files/archive/urbis/images/823.jpg"');
update archive_article set content = replace(content, '<img src="824"', '<img src="/site_media/media/files/archive/urbis/images/824.jpg"');
update archive_article set content = replace(content, '<img src="825"', '<img src="/site_media/media/files/archive/urbis/images/825.jpg"');
update archive_article set content = replace(content, '<img src="826"', '<img src="/site_media/media/files/archive/urbis/images/826.jpg"');
update archive_article set content = replace(content, '<img src="827"', '<img src="/site_media/media/files/archive/urbis/images/827.jpg"');
update archive_article set content = replace(content, '<img src="828"', '<img src="/site_media/media/files/archive/urbis/images/828.jpg"');
update archive_article set content = replace(content, '<img src="829"', '<img src="/site_media/media/files/archive/urbis/images/829.jpg"');
update archive_article set content = replace(content, '<img src="830"', '<img src="/site_media/media/files/archive/urbis/images/830.jpg"');
update archive_article set content = replace(content, '<img src="831"', '<img src="/site_media/media/files/archive/urbis/images/831.jpg"');
update archive_article set content = replace(content, '<img src="832"', '<img src="/site_media/media/files/archive/urbis/images/832.jpg"');
update archive_article set content = replace(content, '<img src="833"', '<img src="/site_media/media/files/archive/urbis/images/833.jpg"');
update archive_article set content = replace(content, '<img src="834"', '<img src="/site_media/media/files/archive/urbis/images/834.jpg"');
update archive_article set content = replace(content, '<img src="835"', '<img src="/site_media/media/files/archive/urbis/images/835.jpg"');
update archive_article set content = replace(content, '<img src="836"', '<img src="/site_media/media/files/archive/urbis/images/836.jpg"');
update archive_article set content = replace(content, '<img src="837"', '<img src="/site_media/media/files/archive/urbis/images/837.jpg"');
update archive_article set content = replace(content, '<img src="838"', '<img src="/site_media/media/files/archive/urbis/images/838.jpg"');
update archive_article set content = replace(content, '<img src="839"', '<img src="/site_media/media/files/archive/urbis/images/839.jpg"');
update archive_article set content = replace(content, '<img src="840"', '<img src="/site_media/media/files/archive/urbis/images/840.jpg"');
update archive_article set content = replace(content, '<img src="841"', '<img src="/site_media/media/files/archive/urbis/images/841.jpg"');
update archive_article set content = replace(content, '<img src="842"', '<img src="/site_media/media/files/archive/urbis/images/842.jpg"');
update archive_article set content = replace(content, '<img src="843"', '<img src="/site_media/media/files/archive/urbis/images/843.jpg"');
update archive_article set content = replace(content, '<img src="844"', '<img src="/site_media/media/files/archive/urbis/images/844.jpg"');
update archive_article set content = replace(content, '<img src="845"', '<img src="/site_media/media/files/archive/urbis/images/845.jpg"');
update archive_article set content = replace(content, '<img src="846"', '<img src="/site_media/media/files/archive/urbis/images/846.jpg"');
update archive_article set content = replace(content, '<img src="847"', '<img src="/site_media/media/files/archive/urbis/images/847.jpg"');
update archive_article set content = replace(content, '<img src="848"', '<img src="/site_media/media/files/archive/urbis/images/848.jpg"');
update archive_article set content = replace(content, '<img src="849"', '<img src="/site_media/media/files/archive/urbis/images/849.jpg"');
update archive_article set content = replace(content, '<img src="850"', '<img src="/site_media/media/files/archive/urbis/images/850.jpg"');
update archive_article set content = replace(content, '<img src="851"', '<img src="/site_media/media/files/archive/urbis/images/851.jpg"');
update archive_article set content = replace(content, '<img src="852"', '<img src="/site_media/media/files/archive/urbis/images/852.jpg"');
update archive_article set content = replace(content, '<img src="853"', '<img src="/site_media/media/files/archive/urbis/images/853.jpg"');
update archive_article set content = replace(content, '<img src="854"', '<img src="/site_media/media/files/archive/urbis/images/854.jpg"');
update archive_article set content = replace(content, '<img src="855"', '<img src="/site_media/media/files/archive/urbis/images/855.jpg"');
update archive_article set content = replace(content, '<img src="861"', '<img src="/site_media/media/files/archive/urbis/images/861.jpg"');
update archive_article set content = replace(content, '<img src="857"', '<img src="/site_media/media/files/archive/urbis/images/857.jpg"');
update archive_article set content = replace(content, '<img src="858"', '<img src="/site_media/media/files/archive/urbis/images/858.jpg"');
update archive_article set content = replace(content, '<img src="859"', '<img src="/site_media/media/files/archive/urbis/images/859.jpg"');
update archive_article set content = replace(content, '<img src="860"', '<img src="/site_media/media/files/archive/urbis/images/860.gif"');
update archive_article set content = replace(content, '<img src="862"', '<img src="/site_media/media/files/archive/urbis/images/862.jpg"');
update archive_article set content = replace(content, '<img src="863"', '<img src="/site_media/media/files/archive/urbis/images/863.jpg"');
update archive_article set content = replace(content, '<img src="867"', '<img src="/site_media/media/files/archive/urbis/images/867.jpg"');
update archive_article set content = replace(content, '<img src="866"', '<img src="/site_media/media/files/archive/urbis/images/866.jpg"');
update archive_article set content = replace(content, '<img src="871"', '<img src="/site_media/media/files/archive/urbis/images/871.jpg"');
update archive_article set content = replace(content, '<img src="869"', '<img src="/site_media/media/files/archive/urbis/images/869.jpg"');
update archive_article set content = replace(content, '<img src="870"', '<img src="/site_media/media/files/archive/urbis/images/870.jpg"');
update archive_article set content = replace(content, '<img src="872"', '<img src="/site_media/media/files/archive/urbis/images/872.jpg"');
update archive_article set content = replace(content, '<img src="873"', '<img src="/site_media/media/files/archive/urbis/images/873.jpg"');
update archive_article set content = replace(content, '<img src="874"', '<img src="/site_media/media/files/archive/urbis/images/874.jpg"');
update archive_article set content = replace(content, '<img src="875"', '<img src="/site_media/media/files/archive/urbis/images/875.jpg"');
update archive_article set content = replace(content, '<img src="876"', '<img src="/site_media/media/files/archive/urbis/images/876.png"');
update archive_article set content = replace(content, '<img src="877"', '<img src="/site_media/media/files/archive/urbis/images/877.jpg"');
update archive_article set content = replace(content, '<img src="878"', '<img src="/site_media/media/files/archive/urbis/images/878.jpg"');
update archive_article set content = replace(content, '<img src="879"', '<img src="/site_media/media/files/archive/urbis/images/879.jpg"');
update archive_article set content = replace(content, '<img src="880"', '<img src="/site_media/media/files/archive/urbis/images/880.jpg"');
update archive_article set content = replace(content, '<img src="881"', '<img src="/site_media/media/files/archive/urbis/images/881.jpg"');
update archive_article set content = replace(content, '<img src="882"', '<img src="/site_media/media/files/archive/urbis/images/882.jpg"');
update archive_article set content = replace(content, '<img src="883"', '<img src="/site_media/media/files/archive/urbis/images/883.jpg"');
update archive_article set content = replace(content, '<img src="884"', '<img src="/site_media/media/files/archive/urbis/images/884.jpg"');
update archive_article set content = replace(content, '<img src="885"', '<img src="/site_media/media/files/archive/urbis/images/885.jpg"');
update archive_article set content = replace(content, '<img src="886"', '<img src="/site_media/media/files/archive/urbis/images/886.jpg"');
update archive_article set content = replace(content, '<img src="887"', '<img src="/site_media/media/files/archive/urbis/images/887.jpg"');
update archive_article set content = replace(content, '<img src="888"', '<img src="/site_media/media/files/archive/urbis/images/888.jpg"');
update archive_article set content = replace(content, '<img src="889"', '<img src="/site_media/media/files/archive/urbis/images/889.jpg"');
update archive_article set content = replace(content, '<img src="890"', '<img src="/site_media/media/files/archive/urbis/images/890.jpg"');
update archive_article set content = replace(content, '<img src="891"', '<img src="/site_media/media/files/archive/urbis/images/891.jpg"');
update archive_article set content = replace(content, '<img src="892"', '<img src="/site_media/media/files/archive/urbis/images/892.jpg"');
update archive_article set content = replace(content, '<img src="893"', '<img src="/site_media/media/files/archive/urbis/images/893.jpg"');
update archive_article set content = replace(content, '<img src="894"', '<img src="/site_media/media/files/archive/urbis/images/894.jpg"');
update archive_article set content = replace(content, '<img src="895"', '<img src="/site_media/media/files/archive/urbis/images/895.jpg"');
update archive_article set content = replace(content, '<img src="896"', '<img src="/site_media/media/files/archive/urbis/images/896.jpg"');
update archive_article set content = replace(content, '<img src="897"', '<img src="/site_media/media/files/archive/urbis/images/897.jpg"');
update archive_article set content = replace(content, '<img src="898"', '<img src="/site_media/media/files/archive/urbis/images/898.jpg"');
update archive_article set content = replace(content, '<img src="899"', '<img src="/site_media/media/files/archive/urbis/images/899.jpg"');
update archive_article set content = replace(content, '<img src="900"', '<img src="/site_media/media/files/archive/urbis/images/900.jpg"');
update archive_article set content = replace(content, '<img src="901"', '<img src="/site_media/media/files/archive/urbis/images/901.jpg"');
update archive_article set content = replace(content, '<img src="902"', '<img src="/site_media/media/files/archive/urbis/images/902.jpg"');
update archive_article set content = replace(content, '<img src="903"', '<img src="/site_media/media/files/archive/urbis/images/903.jpg"');
update archive_article set content = replace(content, '<img src="906"', '<img src="/site_media/media/files/archive/urbis/images/906.jpg"');
update archive_article set content = replace(content, '<img src="905"', '<img src="/site_media/media/files/archive/urbis/images/905.jpg"');
update archive_article set content = replace(content, '<img src="907"', '<img src="/site_media/media/files/archive/urbis/images/907.jpg"');
update archive_article set content = replace(content, '<img src="908"', '<img src="/site_media/media/files/archive/urbis/images/908.jpg"');
update archive_article set content = replace(content, '<img src="909"', '<img src="/site_media/media/files/archive/urbis/images/909.jpg"');
update archive_article set content = replace(content, '<img src="911"', '<img src="/site_media/media/files/archive/urbis/images/911.jpg"');
update archive_article set content = replace(content, '<img src="912"', '<img src="/site_media/media/files/archive/urbis/images/912.jpg"');
update archive_article set content = replace(content, '<img src="913"', '<img src="/site_media/media/files/archive/urbis/images/913.jpg"');
update archive_article set content = replace(content, '<img src="914"', '<img src="/site_media/media/files/archive/urbis/images/914.jpg"');
update archive_article set content = replace(content, '<img src="915"', '<img src="/site_media/media/files/archive/urbis/images/915.jpg"');
update archive_article set content = replace(content, '<img src="916"', '<img src="/site_media/media/files/archive/urbis/images/916.jpg"');
update archive_article set content = replace(content, '<img src="917"', '<img src="/site_media/media/files/archive/urbis/images/917.jpg"');
update archive_article set content = replace(content, '<img src="918"', '<img src="/site_media/media/files/archive/urbis/images/918.jpg"');
update archive_article set content = replace(content, '<img src="919"', '<img src="/site_media/media/files/archive/urbis/images/919.jpg"');
update archive_article set content = replace(content, '<img src="920"', '<img src="/site_media/media/files/archive/urbis/images/920.jpg"');
update archive_article set content = replace(content, '<img src="921"', '<img src="/site_media/media/files/archive/urbis/images/921.jpg"');
update archive_article set content = replace(content, '<img src="922"', '<img src="/site_media/media/files/archive/urbis/images/922.jpg"');
update archive_article set content = replace(content, '<img src="923"', '<img src="/site_media/media/files/archive/urbis/images/923.jpg"');
update archive_article set content = replace(content, '<img src="924"', '<img src="/site_media/media/files/archive/urbis/images/924.jpg"');
update archive_article set content = replace(content, '<img src="925"', '<img src="/site_media/media/files/archive/urbis/images/925.jpg"');
update archive_article set content = replace(content, '<img src="926"', '<img src="/site_media/media/files/archive/urbis/images/926.jpg"');
update archive_article set content = replace(content, '<img src="927"', '<img src="/site_media/media/files/archive/urbis/images/927.jpg"');
update archive_article set content = replace(content, '<img src="932"', '<img src="/site_media/media/files/archive/urbis/images/932.jpg"');
update archive_article set content = replace(content, '<img src="931"', '<img src="/site_media/media/files/archive/urbis/images/931.jpg"');
update archive_article set content = replace(content, '<img src="933"', '<img src="/site_media/media/files/archive/urbis/images/933.jpg"');
update archive_article set content = replace(content, '<img src="934"', '<img src="/site_media/media/files/archive/urbis/images/934.jpg"');
update archive_article set content = replace(content, '<img src="935"', '<img src="/site_media/media/files/archive/urbis/images/935.jpg"');
update archive_article set content = replace(content, '<img src="936"', '<img src="/site_media/media/files/archive/urbis/images/936.jpg"');
update archive_article set content = replace(content, '<img src="937"', '<img src="/site_media/media/files/archive/urbis/images/937.jpg"');
update archive_article set content = replace(content, '<img src="938"', '<img src="/site_media/media/files/archive/urbis/images/938.jpg"');
update archive_article set content = replace(content, '<img src="939"', '<img src="/site_media/media/files/archive/urbis/images/939.jpg"');
update archive_article set content = replace(content, '<img src="940"', '<img src="/site_media/media/files/archive/urbis/images/940.jpg"');
update archive_article set content = replace(content, '<img src="941"', '<img src="/site_media/media/files/archive/urbis/images/941.jpg"');
update archive_article set content = replace(content, '<img src="942"', '<img src="/site_media/media/files/archive/urbis/images/942.jpg"');
update archive_article set content = replace(content, '<img src="943"', '<img src="/site_media/media/files/archive/urbis/images/943.jpg"');
update archive_article set content = replace(content, '<img src="944"', '<img src="/site_media/media/files/archive/urbis/images/944.jpg"');
update archive_article set content = replace(content, '<img src="947"', '<img src="/site_media/media/files/archive/urbis/images/947.jpg"');
update archive_article set content = replace(content, '<img src="946"', '<img src="/site_media/media/files/archive/urbis/images/946.jpg"');
update archive_article set content = replace(content, '<img src="948"', '<img src="/site_media/media/files/archive/urbis/images/948.jpg"');
update archive_article set content = replace(content, '<img src="949"', '<img src="/site_media/media/files/archive/urbis/images/949.jpg"');
update archive_article set content = replace(content, '<img src="950"', '<img src="/site_media/media/files/archive/urbis/images/950.jpg"');
update archive_article set content = replace(content, '<img src="951"', '<img src="/site_media/media/files/archive/urbis/images/951.jpg"');
update archive_article set content = replace(content, '<img src="952"', '<img src="/site_media/media/files/archive/urbis/images/952.jpg"');
update archive_article set content = replace(content, '<img src="953"', '<img src="/site_media/media/files/archive/urbis/images/953.jpg"');
update archive_article set content = replace(content, '<img src="954"', '<img src="/site_media/media/files/archive/urbis/images/954.jpg"');
update archive_article set content = replace(content, '<img src="955"', '<img src="/site_media/media/files/archive/urbis/images/955.jpg"');
update archive_article set content = replace(content, '<img src="959"', '<img src="/site_media/media/files/archive/urbis/images/959.jpg"');
update archive_article set content = replace(content, '<img src="960"', '<img src="/site_media/media/files/archive/urbis/images/960.jpg"');
update archive_article set content = replace(content, '<img src="958"', '<img src="/site_media/media/files/archive/urbis/images/958.jpg"');
update archive_article set content = replace(content, '<img src="961"', '<img src="/site_media/media/files/archive/urbis/images/961.jpg"');
update archive_article set content = replace(content, '<img src="962"', '<img src="/site_media/media/files/archive/urbis/images/962.jpg"');
update archive_article set content = replace(content, '<img src="963"', '<img src="/site_media/media/files/archive/urbis/images/963.jpg"');
update archive_article set content = replace(content, '<img src="964"', '<img src="/site_media/media/files/archive/urbis/images/964.jpg"');
update archive_article set content = replace(content, '<img src="965"', '<img src="/site_media/media/files/archive/urbis/images/965.jpg"');
update archive_article set content = replace(content, '<img src="966"', '<img src="/site_media/media/files/archive/urbis/images/966.jpg"');
update archive_article set content = replace(content, '<img src="967"', '<img src="/site_media/media/files/archive/urbis/images/967.jpg"');
update archive_article set content = replace(content, '<img src="968"', '<img src="/site_media/media/files/archive/urbis/images/968.jpg"');
update archive_article set content = replace(content, '<img src="969"', '<img src="/site_media/media/files/archive/urbis/images/969.jpg"');
update archive_article set content = replace(content, '<img src="970"', '<img src="/site_media/media/files/archive/urbis/images/970.jpg"');
update archive_article set content = replace(content, '<img src="971"', '<img src="/site_media/media/files/archive/urbis/images/971.jpg"');
update archive_article set content = replace(content, '<img src="972"', '<img src="/site_media/media/files/archive/urbis/images/972.jpg"');
update archive_article set content = replace(content, '<img src="973"', '<img src="/site_media/media/files/archive/urbis/images/973.jpg"');
update archive_article set content = replace(content, '<img src="974"', '<img src="/site_media/media/files/archive/urbis/images/974.jpg"');
update archive_article set content = replace(content, '<img src="975"', '<img src="/site_media/media/files/archive/urbis/images/975.jpg"');
update archive_article set content = replace(content, '<img src="976"', '<img src="/site_media/media/files/archive/urbis/images/976.jpg"');
update archive_article set content = replace(content, '<img src="977"', '<img src="/site_media/media/files/archive/urbis/images/977.jpg"');
update archive_article set content = replace(content, '<img src="978"', '<img src="/site_media/media/files/archive/urbis/images/978.jpg"');
update archive_article set content = replace(content, '<img src="979"', '<img src="/site_media/media/files/archive/urbis/images/979.jpg"');
update archive_article set content = replace(content, '<img src="980"', '<img src="/site_media/media/files/archive/urbis/images/980.jpg"');
update archive_article set content = replace(content, '<img src="981"', '<img src="/site_media/media/files/archive/urbis/images/981.jpg"');
update archive_article set content = replace(content, '<img src="982"', '<img src="/site_media/media/files/archive/urbis/images/982.jpg"');
update archive_article set content = replace(content, '<img src="983"', '<img src="/site_media/media/files/archive/urbis/images/983.jpg"');
update archive_article set content = replace(content, '<img src="984"', '<img src="/site_media/media/files/archive/urbis/images/984.jpg"');
update archive_article set content = replace(content, '<img src="985"', '<img src="/site_media/media/files/archive/urbis/images/985.jpg"');
update archive_article set content = replace(content, '<img src="986"', '<img src="/site_media/media/files/archive/urbis/images/986.jpg"');
update archive_article set content = replace(content, '<img src="987"', '<img src="/site_media/media/files/archive/urbis/images/987.jpg"');
update archive_article set content = replace(content, '<img src="988"', '<img src="/site_media/media/files/archive/urbis/images/988.jpg"');
update archive_article set content = replace(content, '<img src="989"', '<img src="/site_media/media/files/archive/urbis/images/989.jpg"');
update archive_article set content = replace(content, '<img src="990"', '<img src="/site_media/media/files/archive/urbis/images/990.jpg"');
update archive_article set content = replace(content, '<img src="991"', '<img src="/site_media/media/files/archive/urbis/images/991.jpg"');
update archive_article set content = replace(content, '<img src="992"', '<img src="/site_media/media/files/archive/urbis/images/992.jpg"');
update archive_article set content = replace(content, '<img src="993"', '<img src="/site_media/media/files/archive/urbis/images/993.jpg"');
update archive_article set content = replace(content, '<img src="994"', '<img src="/site_media/media/files/archive/urbis/images/994.jpg"');
update archive_article set content = replace(content, '<img src="995"', '<img src="/site_media/media/files/archive/urbis/images/995.jpg"');
update archive_article set content = replace(content, '<img src="996"', '<img src="/site_media/media/files/archive/urbis/images/996.jpg"');
update archive_article set content = replace(content, '<img src="997"', '<img src="/site_media/media/files/archive/urbis/images/997.jpg"');
update archive_article set content = replace(content, '<img src="998"', '<img src="/site_media/media/files/archive/urbis/images/998.jpg"');
update archive_article set content = replace(content, '<img src="999"', '<img src="/site_media/media/files/archive/urbis/images/999.jpg"');
update archive_article set content = replace(content, '<img src="1000"', '<img src="/site_media/media/files/archive/urbis/images/1000.jpg"');
update archive_article set content = replace(content, '<img src="1001"', '<img src="/site_media/media/files/archive/urbis/images/1001.jpg"');
update archive_article set content = replace(content, '<img src="1008"', '<img src="/site_media/media/files/archive/urbis/images/1008.jpg"');
update archive_article set content = replace(content, '<img src="1007"', '<img src="/site_media/media/files/archive/urbis/images/1007.jpg"');
update archive_article set content = replace(content, '<img src="1009"', '<img src="/site_media/media/files/archive/urbis/images/1009.jpg"');
update archive_article set content = replace(content, '<img src="1010"', '<img src="/site_media/media/files/archive/urbis/images/1010.jpg"');
update archive_article set content = replace(content, '<img src="1011"', '<img src="/site_media/media/files/archive/urbis/images/1011.jpg"');
update archive_article set content = replace(content, '<img src="1012"', '<img src="/site_media/media/files/archive/urbis/images/1012.jpg"');
update archive_article set content = replace(content, '<img src="1013"', '<img src="/site_media/media/files/archive/urbis/images/1013.jpg"');
update archive_article set content = replace(content, '<img src="1014"', '<img src="/site_media/media/files/archive/urbis/images/1014.jpg"');
update archive_article set content = replace(content, '<img src="1015"', '<img src="/site_media/media/files/archive/urbis/images/1015.jpg"');
update archive_article set content = replace(content, '<img src="1016"', '<img src="/site_media/media/files/archive/urbis/images/1016.jpg"');
update archive_article set content = replace(content, '<img src="1017"', '<img src="/site_media/media/files/archive/urbis/images/1017.jpg"');
update archive_article set content = replace(content, '<img src="1018"', '<img src="/site_media/media/files/archive/urbis/images/1018.jpg"');
update archive_article set content = replace(content, '<img src="1019"', '<img src="/site_media/media/files/archive/urbis/images/1019.jpg"');
update archive_article set content = replace(content, '<img src="1020"', '<img src="/site_media/media/files/archive/urbis/images/1020.jpg"');
update archive_article set content = replace(content, '<img src="1021"', '<img src="/site_media/media/files/archive/urbis/images/1021.jpg"');
update archive_article set content = replace(content, '<img src="1022"', '<img src="/site_media/media/files/archive/urbis/images/1022.jpg"');
update archive_article set content = replace(content, '<img src="1023"', '<img src="/site_media/media/files/archive/urbis/images/1023.jpg"');
update archive_article set content = replace(content, '<img src="1024"', '<img src="/site_media/media/files/archive/urbis/images/1024.jpg"');
update archive_article set content = replace(content, '<img src="1025"', '<img src="/site_media/media/files/archive/urbis/images/1025.jpg"');
update archive_article set content = replace(content, '<img src="1026"', '<img src="/site_media/media/files/archive/urbis/images/1026.jpg"');
update archive_article set content = replace(content, '<img src="1027"', '<img src="/site_media/media/files/archive/urbis/images/1027.jpg"');
update archive_article set content = replace(content, '<img src="1028"', '<img src="/site_media/media/files/archive/urbis/images/1028.jpg"');
update archive_article set content = replace(content, '<img src="1029"', '<img src="/site_media/media/files/archive/urbis/images/1029.jpg"');
update archive_article set content = replace(content, '<img src="1034"', '<img src="/site_media/media/files/archive/urbis/images/1034.jpg"');
update archive_article set content = replace(content, '<img src="1033"', '<img src="/site_media/media/files/archive/urbis/images/1033.jpg"');
update archive_article set content = replace(content, '<img src="1035"', '<img src="/site_media/media/files/archive/urbis/images/1035.jpg"');
update archive_article set content = replace(content, '<img src="1036"', '<img src="/site_media/media/files/archive/urbis/images/1036.jpg"');
update archive_article set content = replace(content, '<img src="1037"', '<img src="/site_media/media/files/archive/urbis/images/1037.jpg"');
update archive_article set content = replace(content, '<img src="1038"', '<img src="/site_media/media/files/archive/urbis/images/1038.jpg"');
update archive_article set content = replace(content, '<img src="1039"', '<img src="/site_media/media/files/archive/urbis/images/1039.jpg"');
update archive_article set content = replace(content, '<img src="1040"', '<img src="/site_media/media/files/archive/urbis/images/1040.jpg"');
update archive_article set content = replace(content, '<img src="1041"', '<img src="/site_media/media/files/archive/urbis/images/1041.jpg"');
update archive_article set content = replace(content, '<img src="1042"', '<img src="/site_media/media/files/archive/urbis/images/1042.jpg"');
update archive_article set content = replace(content, '<img src="1043"', '<img src="/site_media/media/files/archive/urbis/images/1043.jpg"');
update archive_article set content = replace(content, '<img src="1044"', '<img src="/site_media/media/files/archive/urbis/images/1044.jpg"');
update archive_article set content = replace(content, '<img src="1045"', '<img src="/site_media/media/files/archive/urbis/images/1045.jpg"');
update archive_article set content = replace(content, '<img src="1046"', '<img src="/site_media/media/files/archive/urbis/images/1046.jpg"');
update archive_article set content = replace(content, '<img src="1047"', '<img src="/site_media/media/files/archive/urbis/images/1047.jpg"');
update archive_article set content = replace(content, '<img src="1048"', '<img src="/site_media/media/files/archive/urbis/images/1048.jpg"');
update archive_article set content = replace(content, '<img src="1049"', '<img src="/site_media/media/files/archive/urbis/images/1049.jpg"');
update archive_article set content = replace(content, '<img src="1050"', '<img src="/site_media/media/files/archive/urbis/images/1050.jpg"');
update archive_article set content = replace(content, '<img src="1051"', '<img src="/site_media/media/files/archive/urbis/images/1051.jpg"');
update archive_article set content = replace(content, '<img src="1052"', '<img src="/site_media/media/files/archive/urbis/images/1052.jpg"');
update archive_article set content = replace(content, '<img src="1053"', '<img src="/site_media/media/files/archive/urbis/images/1053.jpg"');
update archive_article set content = replace(content, '<img src="1054"', '<img src="/site_media/media/files/archive/urbis/images/1054.jpg"');
update archive_article set content = replace(content, '<img src="1055"', '<img src="/site_media/media/files/archive/urbis/images/1055.jpg"');
update archive_article set content = replace(content, '<img src="1056"', '<img src="/site_media/media/files/archive/urbis/images/1056.jpg"');
update archive_article set content = replace(content, '<img src="1057"', '<img src="/site_media/media/files/archive/urbis/images/1057.jpg"');
update archive_article set content = replace(content, '<img src="1058"', '<img src="/site_media/media/files/archive/urbis/images/1058.jpg"');
update archive_article set content = replace(content, '<img src="1059"', '<img src="/site_media/media/files/archive/urbis/images/1059.jpg"');
update archive_article set content = replace(content, '<img src="1060"', '<img src="/site_media/media/files/archive/urbis/images/1060.jpg"');
update archive_article set content = replace(content, '<img src="1061"', '<img src="/site_media/media/files/archive/urbis/images/1061.jpg"');
update archive_article set content = replace(content, '<img src="1062"', '<img src="/site_media/media/files/archive/urbis/images/1062.jpg"');
update archive_article set content = replace(content, '<img src="1063"', '<img src="/site_media/media/files/archive/urbis/images/1063.jpg"');
update archive_article set content = replace(content, '<img src="1064"', '<img src="/site_media/media/files/archive/urbis/images/1064.jpg"');
update archive_article set content = replace(content, '<img src="1065"', '<img src="/site_media/media/files/archive/urbis/images/1065.jpg"');
update archive_article set content = replace(content, '<img src="1066"', '<img src="/site_media/media/files/archive/urbis/images/1066.jpg"');
update archive_article set content = replace(content, '<img src="1067"', '<img src="/site_media/media/files/archive/urbis/images/1067.jpg"');
update archive_article set content = replace(content, '<img src="1068"', '<img src="/site_media/media/files/archive/urbis/images/1068.jpg"');
update archive_article set content = replace(content, '<img src="1069"', '<img src="/site_media/media/files/archive/urbis/images/1069.jpg"');
update archive_article set content = replace(content, '<img src="1070"', '<img src="/site_media/media/files/archive/urbis/images/1070.jpg"');
update archive_article set content = replace(content, '<img src="1071"', '<img src="/site_media/media/files/archive/urbis/images/1071.jpg"');
update archive_article set content = replace(content, '<img src="1072"', '<img src="/site_media/media/files/archive/urbis/images/1072.jpg"');
update archive_article set content = replace(content, '<img src="1073"', '<img src="/site_media/media/files/archive/urbis/images/1073.jpg"');
update archive_article set content = replace(content, '<img src="1074"', '<img src="/site_media/media/files/archive/urbis/images/1074.jpg"');
update archive_article set content = replace(content, '<img src="1075"', '<img src="/site_media/media/files/archive/urbis/images/1075.jpg"');
update archive_article set content = replace(content, '<img src="1076"', '<img src="/site_media/media/files/archive/urbis/images/1076.jpg"');
update archive_article set content = replace(content, '<img src="1077"', '<img src="/site_media/media/files/archive/urbis/images/1077.jpg"');
update archive_article set content = replace(content, '<img src="1078"', '<img src="/site_media/media/files/archive/urbis/images/1078.jpg"');
update archive_article set content = replace(content, '<img src="1079"', '<img src="/site_media/media/files/archive/urbis/images/1079.jpg"');
update archive_article set content = replace(content, '<img src="1080"', '<img src="/site_media/media/files/archive/urbis/images/1080.jpg"');
update archive_article set content = replace(content, '<img src="1081"', '<img src="/site_media/media/files/archive/urbis/images/1081.jpg"');
update archive_article set content = replace(content, '<img src="1082"', '<img src="/site_media/media/files/archive/urbis/images/1082.jpg"');
update archive_article set content = replace(content, '<img src="1083"', '<img src="/site_media/media/files/archive/urbis/images/1083.jpg"');
update archive_article set content = replace(content, '<img src="1084"', '<img src="/site_media/media/files/archive/urbis/images/1084.jpg"');
update archive_article set content = replace(content, '<img src="1085"', '<img src="/site_media/media/files/archive/urbis/images/1085.jpg"');
update archive_article set content = replace(content, '<img src="1086"', '<img src="/site_media/media/files/archive/urbis/images/1086.jpg"');
update archive_article set content = replace(content, '<img src="1087"', '<img src="/site_media/media/files/archive/urbis/images/1087.jpg"');
update archive_article set content = replace(content, '<img src="1088"', '<img src="/site_media/media/files/archive/urbis/images/1088.jpg"');
update archive_article set content = replace(content, '<img src="1089"', '<img src="/site_media/media/files/archive/urbis/images/1089.jpg"');
update archive_article set content = replace(content, '<img src="1090"', '<img src="/site_media/media/files/archive/urbis/images/1090.jpg"');
update archive_article set content = replace(content, '<img src="1097"', '<img src="/site_media/media/files/archive/urbis/images/1097.jpg"');
update archive_article set content = replace(content, '<img src="1092"', '<img src="/site_media/media/files/archive/urbis/images/1092.jpg"');
update archive_article set content = replace(content, '<img src="1093"', '<img src="/site_media/media/files/archive/urbis/images/1093.jpg"');
update archive_article set content = replace(content, '<img src="1094"', '<img src="/site_media/media/files/archive/urbis/images/1094.jpg"');
update archive_article set content = replace(content, '<img src="1095"', '<img src="/site_media/media/files/archive/urbis/images/1095.jpg"');
update archive_article set content = replace(content, '<img src="1096"', '<img src="/site_media/media/files/archive/urbis/images/1096.jpg"');
update archive_article set content = replace(content, '<img src="1098"', '<img src="/site_media/media/files/archive/urbis/images/1098.jpg"');
update archive_article set content = replace(content, '<img src="1099"', '<img src="/site_media/media/files/archive/urbis/images/1099.jpg"');
update archive_article set content = replace(content, '<img src="1100"', '<img src="/site_media/media/files/archive/urbis/images/1100.jpg"');
update archive_article set content = replace(content, '<img src="1101"', '<img src="/site_media/media/files/archive/urbis/images/1101.jpg"');
update archive_article set content = replace(content, '<img src="1102"', '<img src="/site_media/media/files/archive/urbis/images/1102.jpg"');
update archive_article set content = replace(content, '<img src="1103"', '<img src="/site_media/media/files/archive/urbis/images/1103.jpg"');
update archive_article set content = replace(content, '<img src="1104"', '<img src="/site_media/media/files/archive/urbis/images/1104.jpg"');
update archive_article set content = replace(content, '<img src="1105"', '<img src="/site_media/media/files/archive/urbis/images/1105.jpg"');
update archive_article set content = replace(content, '<img src="1106"', '<img src="/site_media/media/files/archive/urbis/images/1106.jpg"');

-- now update  the issue slugs and names for magazine issues
update publications_magazineissue
set
    slug = replace(slug, 'issue', 'issue-')
where slug not like '%-%';

update publications_magazineissue
set
    issue_name = replace(issue_name, 'issue', 'Issue ')
where issue_name not like 'Issue %';

update publications_magazineissue
set
    issue_name = replace(issue_name, '-', ' ')
where issue_name like 'Issue%-%';

update publications_magazineissue
set
    slug = lower(slug);

update publications_magazineissue
set
    issue_name = replace(issue_name, '  ', ' ');

-- now update the issues with the provided issue data data
update publications_magazineissue set issue_year = '2011', issue_month = date_format(str_to_date('2000-FEB-01', '%Y-%b-%e'), '%b')     where issue_number =   60  ;
update publications_magazineissue set issue_year = '2010', issue_month = date_format(str_to_date('2000-DEC-01', '%Y-%b-%e'), '%b')     where issue_number =   59  ;
update publications_magazineissue set issue_year = '2010', issue_month = date_format(str_to_date('2000-OCT-01', '%Y-%b-%e'), '%b')     where issue_number =   58  ;
update publications_magazineissue set issue_year = '2010', issue_month = date_format(str_to_date('2000-AUG-01', '%Y-%b-%e'), '%b')     where issue_number =   57  ;
update publications_magazineissue set issue_year = '2010', issue_month = date_format(str_to_date('2000-JUN-01', '%Y-%b-%e'), '%b')     where issue_number =   56  ;
update publications_magazineissue set issue_year = '2010', issue_month = date_format(str_to_date('2000-APR-01', '%Y-%b-%e'), '%b')     where issue_number =   55  ;
update publications_magazineissue set issue_year = '2010', issue_month = date_format(str_to_date('2000-FEB-01', '%Y-%b-%e'), '%b')     where issue_number =   54  ;
update publications_magazineissue set issue_year = '2009', issue_month = date_format(str_to_date('2000-DEC-01', '%Y-%b-%e'), '%b')     where issue_number =   53  ;
update publications_magazineissue set issue_year = '2009', issue_month = date_format(str_to_date('2000-OCT-01', '%Y-%b-%e'), '%b')     where issue_number =   52  ;
update publications_magazineissue set issue_year = '2009', issue_month = date_format(str_to_date('2000-AUG-01', '%Y-%b-%e'), '%b')     where issue_number =   51  ;
update publications_magazineissue set issue_year = '2009', issue_month = date_format(str_to_date('2000-JUN-01', '%Y-%b-%e'), '%b')     where issue_number =   50  ;
update publications_magazineissue set issue_year = '2009', issue_month = date_format(str_to_date('2000-APR-01', '%Y-%b-%e'), '%b')     where issue_number =   49  ;
update publications_magazineissue set issue_year = '2009', issue_month = date_format(str_to_date('2000-FEB-01', '%Y-%b-%e'), '%b')     where issue_number =   48  ;
update publications_magazineissue set issue_year = '2008', issue_month = date_format(str_to_date('2000-DEC-01', '%Y-%b-%e'), '%b')     where issue_number =   47  ;
update publications_magazineissue set issue_year = '2008', issue_month = date_format(str_to_date('2000-OCT-01', '%Y-%b-%e'), '%b')     where issue_number =   46  ;
update publications_magazineissue set issue_year = '2008', issue_month = date_format(str_to_date('2000-AUG-01', '%Y-%b-%e'), '%b')     where issue_number =   45  ;
update publications_magazineissue set issue_year = '2008', issue_month = date_format(str_to_date('2000-JUN-01', '%Y-%b-%e'), '%b')     where issue_number =   44  ;
update publications_magazineissue set issue_year = '2008', issue_month = date_format(str_to_date('2000-APR-01', '%Y-%b-%e'), '%b')     where issue_number =   43  ;
update publications_magazineissue set issue_year = '2008', issue_month = date_format(str_to_date('2000-FEB-01', '%Y-%b-%e'), '%b')     where issue_number =   42  ;
update publications_magazineissue set issue_year = '2007', issue_month = date_format(str_to_date('2000-DEC-01', '%Y-%b-%e'), '%b')     where issue_number =   41  ;
update publications_magazineissue set issue_year = '2007', issue_month = date_format(str_to_date('2000-OCT-01', '%Y-%b-%e'), '%b')     where issue_number =   40  ;
update publications_magazineissue set issue_year = '2007', issue_month = date_format(str_to_date('2000-AUG-01', '%Y-%b-%e'), '%b')     where issue_number =   39  ;
update publications_magazineissue set issue_year = '2007', issue_month = date_format(str_to_date('2000-JUN-01', '%Y-%b-%e'), '%b')     where issue_number =   38  ;
update publications_magazineissue set issue_year = '2007', issue_month = date_format(str_to_date('2000-APR-01', '%Y-%b-%e'), '%b')     where issue_number =   37  ;
update publications_magazineissue set issue_year = '2007', issue_month = date_format(str_to_date('2000-FEB-01', '%Y-%b-%e'), '%b')     where issue_number =   36  ;
update publications_magazineissue set issue_year = '2007', issue_month = date_format(str_to_date('2000-JAN-01', '%Y-%b-%e'), '%b')     where issue_number =   35  ;
update publications_magazineissue set issue_year = '2006', issue_month = date_format(str_to_date('2000-DEC-01', '%Y-%b-%e'), '%b')     where issue_number =   34  ;
update publications_magazineissue set issue_year = '2006', issue_month = date_format(str_to_date('2000-NOV-01', '%Y-%b-%e'), '%b')     where issue_number =   33  ;
update publications_magazineissue set issue_year = '2006', issue_month = date_format(str_to_date('2000-OCT-01', '%Y-%b-%e'), '%b')     where issue_number =   32  ;
update publications_magazineissue set issue_year = '2006', issue_month = date_format(str_to_date('2000-SEP-01', '%Y-%b-%e'), '%b')     where issue_number =   31  ;

-- now drop all the urbis temporary tables
drop table tmp_textpattern;
drop table tmp_txp_image;

-- END: urbis data


-- START: architecture australia data

-- import the archive data in temporary tables. stage it up basically
\. stage_up_architecture_australia_archive_data.sql

-- just grab the row for the architecture australia magazine and whack it in the publications_magazine table
insert ignore into publications_magazine set title='Architecture Australia', slug='architecture-australia', show_issues = 1;

-- seed the magazine section table with what was known as article types in the old system

-- cop the article section data across
insert into archive_article
(
    id,
    title,
    slug,
    content,
    magazine_section_id,
    introduction,
    issue_id,
    credit,
    review,
    type_string,
    summary
)
select
    tmp.id,
    tmp.title,
    tmp.slug,
    replace(tmp.content, 'http://content.architecturemedia.com/resources/aa/', '/site_media/media/files/archive/architecture_australia/images/'),
    tmp.article_type_id,
    tmp.introduction,
    tmp.issue_id,
    tmp.credit,
    tmp.review,
    tmp.type_string,
    tmp.summary
from
    tmp_article tmp;

-- copy the article section data across
insert into archive_articlesection
(
    id,
    archive_article_id,
    heading,
    bold_text,
    body,
    author_description,
    orig_body,
    template
)
select
    tmp.id,
    tmp.article_id,
    tmp.heading,
    tmp.bold_text,
    replace(tmp.body, 'http://content.architecturemedia.com/resources/aa/', '/site_media/media/files/archive/architecture_australia/images/'),
    tmp.author_description,
    tmp.orig_body,
    tmp.template
from
    tmp_articlesection tmp;
    
-- copy the article section image data across
insert into archive_articlesectionimage
(
    id,
    archive_article_section_id,
    url,
    sequence,
    caption
)
select
    tmp.id,
    tmp.section_id,
    replace(tmp.url, 'http://content.architecturemedia.com/resources/aa/', 'files/archive/architecture_australia/images/'),
    tmp.sequence,
    tmp.caption
from
    tmp_articlesectionimage tmp;

-- now migrate the magazine issue data from the old system into the appropriate table
-- in the new system, with a couple of little translations
insert into publications_magazineissue(
    magazine_id,
    issue_date,
    issue_number,
    issue_month,
    issue_year,
    issue_name,
    slug,
    cover_image)
select 
    (select id from publications_magazine where title='Architecture Australia'), 
    issue_date, 
    issue_number, 
    date_format(concat('1970-',issue_month,'-01'), '%b'),
    issue_year,
    if( issue_month=12, 
            concat('December/January', issue_year),
            concat(
                date_format(
                            concat('1970-', issue_month, '-01'), 
                            '%M'
                           ), 
                '/',
                date_format(
                            concat('1970-', issue_month + 1, '-01'), 
                            '%M'
                            ),
                ' ',
                issue_year
            )
        ),
    lower(
        replace(
            replace(
                    if( issue_month=12, 
                            concat('december-january', issue_year),
                            concat(
                                date_format(
                                            concat('1970-', issue_month, '-01'), 
                                            '%M'
                                           ), 
                                '/',
                                date_format(
                                            concat('1970-', issue_month + 1, '-01'), 
                                            '%M'
                                            ),
                                ' ',
                                issue_year
                            )
                        ),
                    ' ',
                    '-'
                   ),
                   '/',
                   '-' 
                )
         ),
        concat('files/archive/architecture_australia/covers/', issue_year, substring(issue_number, -2), '.jpg')
from tmp_magazineissue;

-- now update the issue_id for the archive articles so that it
-- corresponds to the correct PK value from publications_magazineissue, 
-- using the issue_number to look it up.
update archive_article, publications_magazineissue issues
set
    archive_article.issue_id = issues.id
where
   archive_article.issue_id = issues.issue_number; 


-- now update teh slug
update archive_article
set
    slug = lower(
                    concat(
                            substring(id, -2),
                            '-',
                            slug
                          )
                );

-- now drop all the temporary tables
drop table tmp_article;
drop table tmp_articlesection;
drop table tmp_articlesectionimage;
drop table tmp_magazine;
drop table tmp_magazineissue;

-- END: architecture australia data


-- START: article slug cleanup

-- clean up an dodgy characters
update archive_article set slug = replace(slug, ' ','-');
update archive_article set slug = replace(slug, unhex('A'),'');
update archive_article set slug = replace(slug, unhex('D'),'');
update archive_article set slug = replace(slug, unhex(91),'');
update archive_article set slug = replace(slug, unhex(92),'');
update archive_article set slug = replace(slug, unhex(97),'');
update archive_article set slug = replace(slug, unhex(96),'');
update archive_article set slug = replace(slug, concat(unhex('D'),unhex('A')),'');
update archive_article set slug = replace(slug, '*','');
update archive_article set slug = replace(slug, '@','');
update archive_article set slug = replace(slug, '(','');
update archive_article set slug = replace(slug, '(','');
update archive_article set slug = replace(slug, ':','');
update archive_article set slug = replace(slug, '\'','');
update archive_article set slug = replace(slug, ',','-');
update archive_article set slug = replace(slug, '.','-');
update archive_article set slug = replace(slug, '/','-');
update archive_article set slug = replace(slug, '+','plus');
update archive_article set slug = replace(slug, '--','-');
update archive_article set slug = lower(slug);

-- END: article slug cleanup
