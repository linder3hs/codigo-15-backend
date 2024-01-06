-- AlterTable
ALTER TABLE `products` ADD COLUMN `catagory_id` INTEGER NULL;

-- CreateTable
CREATE TABLE `categories` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `description` TEXT NOT NULL,
    `created_at` DATETIME(3) NOT NULL DEFAULT CURRENT_TIMESTAMP(3),
    `updated_at` DATETIME(3) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `products` ADD CONSTRAINT `products_catagory_id_fkey` FOREIGN KEY (`catagory_id`) REFERENCES `categories`(`id`) ON DELETE SET NULL ON UPDATE CASCADE;
