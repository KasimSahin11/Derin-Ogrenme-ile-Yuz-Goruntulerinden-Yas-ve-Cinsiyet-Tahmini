# Yüz Görüntülerinden Yaş ve Cinsiyet Tahmini
Bu repo, yüz görüntülerinden yaş ve cinsiyet tahmini yapmak için derin öğrenme tekniklerini kullanan bir projeyi içermektedir. Projede üç farklı model kullanılmıştır: özelleştirilmiş bir CNN algoritması, transfer öğrenme ile eğitilmiş ResNet50 ve sıfırdan eğitilmiş ResNet50. Bu modeller UTK-Face veri seti kullanılarak eğitilmiş ve test edilmiştir. Projede yaş ve cinsiyet tahmini performansını artırmak için çeşitli teknikler uygulanmıştır.

## Projenin Amacı
Yüz görüntülerinden yaş ve cinsiyet tahmini, teknolojinin ilerlemesi ve yapay zeka uygulamalarının artmasıyla önem kazanan bir konudur. Bu çalışma, derin öğrenme tekniklerinin bu alandaki etkin kullanımını vurgulayarak, geniş yaş ve cinsiyet gruplarına uygulanabilir ve gerçek dünya koşullarında etkili bir model geliştirmeyi amaçlamaktadır.

## Kullanılan Modeller ve Yöntemler
Projede kullanılan modeller ve yöntemler aşağıda listelenmiştir:

ResNet50 (Transfer Öğrenme): ImageNet veri seti üzerinde eğitilmiş ağırlıklarla başlatılan ve transfer öğrenme teknikleri kullanılarak eğitilen bir model. Bu model, yüksek doğruluk oranları ve düşük kayıp değerleri göstermiştir.

ResNet50 (Transfer Öğrenme Yok): Rastgele başlatılan ağırlıklarla eğitilen bir model. Bu model, transfer öğrenme olmadan da belirli bir başarı düzeyine ulaşabilir.

Özelleştirilmiş CNN Modeli: Özelleştirilmiş katmanlar ve yapılandırmalar kullanarak tasarlanmış bir model.


## Veri Seti
UTKFace veri seti, geniş yaş aralığına ve çeşitli etnik kökenlere sahip 20.000'den fazla yüz görüntüsünü içerir. Veri seti, modelin genelleştirilmesi ve çeşitli demografik gruplarda etkili olması için kullanılmıştır.


## Model Eğitimi ve Sonuçlar
Model eğitimi ve elde edilen sonuçlar hakkında detaylı bilgi, kodların içinde sunulmuştur. Transfer öğrenme ile eğitilen ResNet50 modeli, diğer modellere göre daha yüksek doğruluk oranları ve daha düşük kayıp değerleri sergilemiştir.
