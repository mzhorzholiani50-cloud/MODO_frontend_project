/* პროექტის დემო-კონტენტი — მონაცემები ადვილად შესაცვლელია. */
const PROJECTS = [
  {id:1,title:'Orbit Field', category:'ბრენდინგი', year:2026,client:'Orbit Creative',description:'ვიზუალური იდენტობა კონცეპტუალური შემოქმედებითი სტუდიისთვის. წრეები, კონტრასტები და მოქნილი ლოგოს სისტემა.',services:['ლოგო','ბრენდის სისტემა','არტ-დირექცია']},
  {id:2,title:'Kinetic Type',category:'ტიპოგრაფია',year:2026,client:'Type Lab',description:'ექსპერიმენტული ტიპოგრაფიული პოსტერების სერია, რომელიც ასოების რიტმსა და მოძრაობას იკვლევს.',services:['ტიპოგრაფია','პოსტერი']},
  {id:3,title:'Bloom Club',category:'ილუსტრაცია',year:2026,client:'Bloom Collective',description:'თამამი ფერებითა და ორგანული ფორმებით შექმნილი ილუსტრაციების კოლექცია.',services:['ილუსტრაცია','ფერთა პალიტრა']},
  {id:4,title:'In / Out Space',category:'ვებ-დიზაინი',year:2025,client:'Interior Concept',description:'მინიმალისტური ციფრული კონცეფცია თანამედროვე ინტერიერის სივრცისთვის.',services:['UI დიზაინი','დიზაინ-სისტემა']},
  {id:5,title:'Echo Waves',category:'ილუსტრაცია',year:2026,client:'Echo Studio',description:'ტალღოვანი ხაზებით შექმნილი ვიზუალური ენა, რომელიც მუსიკისა და ხმების იდეას გადმოსცემს.',services:['ილუსტრაცია','პოსტერი']},
  {id:6,title:'Soft Form',category:'ბრენდინგი',year:2025,client:'Soft Studio',description:'მეგობრული და დასამახსოვრებელი ვიზუალური იდენტობა დიზაინის პროდუქტისთვის.',services:['იდენტობა','ფერები']},
  {id:7,title:'Mono Studio',category:'ვებ-დიზაინი',year:2026,client:'Mono Studio',description:'სუფთა ბადე, მკაფიო იერარქია და მოდულური ლენდინგ-გვერდის კონცეფცია.',services:['UX','UI დიზაინი']},
  {id:8,title:'After Image',category:'ტიპოგრაფია',year:2025,client:'After Image',description:'ღამის კულტურის პოსტერების სერია ტიპოგრაფიისა და გეომეტრიის შერწყმით.',services:['პოსტერი','ტიპოგრაფია']},
  {id:9,title:'New Ritual',category:'ბრენდინგი',year:2026,client:'Ritual Studio',description:'ახალი ყოველდღიური რიტუალებისადმი მიძღვნილი თბილი ვიზუალური კონცეფცია.',services:['ბრენდინგი','არტ-დირექცია']},
  {id:10,title:'Off Grid',category:'ვებ-დიზაინი',year:2025,client:'Off Grid Digital',description:'გაბედული ბადე და ნათელი აქცენტები თანამედროვე პროდუქტის გვერდისთვის.',services:['ვებ-დიზაინი','პროტოტიპი']},
  {id:11,title:'Slow Motion',category:'ილუსტრაცია',year:2026,client:'Slow Motion',description:'დინების, სიმშვიდისა და მოძრაობის თემაზე აგებული გრაფიკული ექსპერიმენტი.',services:['ილუსტრაცია','პოსტერი']},
  {id:12,title:'Other Side',category:'ტიპოგრაფია',year:2025,client:'Other Side',description:'გეომეტრიისა და მკაფიო ასოების დახმარებით შექმნილი პოსტერის ახალი ხასიათი.',services:['ტიპოგრაფია','ვიზუალური ენა']}
];
const CATEGORIES = ['ყველა','ბრენდინგი','ვებ-დიზაინი','ილუსტრაცია','ტიპოგრაფია'];
